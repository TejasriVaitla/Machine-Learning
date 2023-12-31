from pydub import AudioSegment
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import shutil
from langchain.vectorstores import Chroma
from mutagen.mp3 import MP3
import simpleaudio as sa
from langchain.document_loaders import PyPDFLoader
import io
import wave
import sys
import speech_recognition as sr
import whisper
import queue
import os
import threading
import torch
import numpy as np
import re
from gtts import gTTS
import openai
import click
import time

import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
running = True


@click.command()
@click.option("--model", default="base", help="Model to use", type=click.Choice(["tiny", "base", "small", "medium", "large"]))
@click.option("--english", default=False, help="Whether to use the English model", is_flag=True, type=bool)
@click.option("--energy", default=300, help="Energy level for the mic to detect", type=int)
@click.option("--pause", default=0.8, help="Pause time before entry ends", type=float)
@click.option("--dynamic_energy", default=False, is_flag=True, help="Flag to enable dynamic energy", type=bool)
@click.option("--wake_word", default="hey computer", help="Wake word to listen for", type=str)
@click.option("--verbose", default=False, help="Whether to print verbose output", is_flag=True, type=bool)

def main(model, english, energy, pause, dynamic_energy, wake_word, verbose):
    if model != "large" and english:
        model = model + ".en"
    audio_model = whisper.load_model(model)
    audio_queue = queue.Queue()
    result_queue = queue.Queue()
    
    threading.Thread(target=record_audio, args=(audio_queue, energy, pause, dynamic_energy,)).start()
    threading.Thread(target=transcribe_forever, args=(audio_queue, result_queue, audio_model, english, wake_word, verbose,)).start()
    vectordb, split_documents = extract_text_from_pdf("SFBU2023Catalog.pdf")
    # print(f"PDF Content: {pdf_content[:500]}")
    threading.Thread(target=reply, args=(result_queue, verbose, vectordb, split_documents)).start()

    global running
    while running:
        print(result_queue.get())

def record_audio(audio_queue, energy, pause, dynamic_energy):
    r = sr.Recognizer()
    r.energy_threshold = energy
    r.pause_threshold = pause
    r.dynamic_energy_threshold = dynamic_energy

    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        i = 0
        while True:
            audio = r.listen(source)
            torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
            audio_data = torch_audio
            audio_queue.put_nowait(audio_data)
            i += 1

def transcribe_forever(audio_queue, result_queue, audio_model, english, wake_word, verbose):
    global running
    while True:
        audio_data = audio_queue.get()
        # Start of transcription
        print(f"Starting transcription at {time.strftime('%X')}")
        if english:
            result = audio_model.transcribe(audio_data, language='english')
        else:
            result = audio_model.transcribe(audio_data)
        
        # End of transcription
        print(f"Finished transcription at {time.strftime('%X')} - Result: {result['text'][:50]}...")
        
        predicted_text = result["text"]

        if "stop" in predicted_text.lower() or "exit" in predicted_text.lower():
            running = False
            print("Exit command received. Stopping transcription.")
            break
        
        if predicted_text.strip().lower().startswith(wake_word.strip().lower()):
            pattern = re.compile(re.escape(wake_word), re.IGNORECASE)
            predicted_text = pattern.sub("", predicted_text).strip()
            punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            predicted_text = predicted_text.translate({ord(i): None for i in punc})
            if verbose:
                print("You said the wake word.. Processing {}...".format(predicted_text))

            result_queue.put_nowait(predicted_text)
        else:
            if verbose:
                print("You did not say the wake word.. Ignoring")

def extract_text_from_pdf(pdf_path):
    # 1. loading pdf documents
    loader = PyPDFLoader(pdf_path)
    page = loader.load()
    chunk_size = 2000
    chunk_overlap = 200
    splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
    split =splitter.split_documents(page)

    persist_directory = 'docs/chroma'
    embed = OpenAIEmbeddings()
        # removung directorya nd content
    if os.path.exists(persist_directory):
        directory_path = f'./{persist_directory}'
        shutil.rmtree(directory_path)

        #creating Vector Store
    vectordb = Chroma.from_documents(
        documents = split,
        embedding = embed,
        persist_directory = persist_directory)
    return vectordb, split


def play_audio(audio_segment):
    # Convert the AudioSegment to a WAV byte stream
    wav_io = io.BytesIO()
    audio_segment.export(wav_io, format='wav')
    wav_io.seek(0)
    wav_data = wav_io.read()

    # Play the audio using simpleaudio
    wave_obj = sa.WaveObject.from_wave_file(io.BytesIO(wav_data))
    play_obj = wave_obj.play()
    play_obj.wait_done()

def query_vectordb(vectordb, question, split_documents):
    answer = vectordb.similarity_search(question)
    return answer

def reply(result_queue, verbose, vectordb, split_documents):
    while True:
        try:
            question = result_queue.get()
            if verbose:
                print(f"[{time.strftime('%X')}] Received question: {question}")

            # Formulate the prompt with additional context or instructions
            relevant_text = query_vectordb(vectordb, question, split_documents)
            combined_input = f"Context from the document: {relevant_text}\nInput: {question}"
            prompt = (
                "Given the following document context and a user's question, provide a detailed and informative answer.\n"
                f"{combined_input}\n"
                "Output:"
            )
            # OpenAI API call
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.5,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            answer = response.choices[0].text.strip()

            # Store the response to a file
            with open("response.txt", "a") as response_file:
                response_file.write(f"User's question: {question}\n")
                response_file.write(f"AI's response: {answer}\n\n")

            # Generate the spoken response and play it
            if verbose:
                print(f"[{time.strftime('%X')}] Generating audio for the response.")
            
            mp3_obj = gTTS(text=answer, lang="en", slow=False)
            mp3_filename = f"response_{time.strftime('%Y%m%d_%H%M%S')}.mp3"
            mp3_obj.save(mp3_filename)
            mp3_fp = io.BytesIO()
            mp3_obj.write_to_fp(mp3_fp)
            mp3_fp.seek(0)

            # Convert MP3 data to WAV and play the response
            sound = AudioSegment.from_file(mp3_fp, format="mp3")
            wav_fp = io.BytesIO()
            sound.export(wav_fp, format="wav")
            wav_fp.seek(0)
            

            if verbose:
                print(f"[{time.strftime('%X')}] Playing the response.")
            play_obj = sa.WaveObject.from_wave_file(wav_fp).play()
            play_obj.wait_done()

        except Exception as e:
            if verbose:
                print(f"[{time.strftime('%X')}] Error processing question: {e}")
        
init_api()
main()
