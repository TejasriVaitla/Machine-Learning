# Generating Answers

## Introduction

The AI Article Assistant is a Python-based tool designed to facilitate the process of finding relevant information from a large text corpus and generating concise answers to user queries. This tool leverages advanced natural language processing techniques and is particularly useful for extracting insights from extensive articles or documents.


## Design

### Preprocessing Input Texts:
The first step involves preprocessing the input texts. The text is split into paragraphs, and any unnecessary spaces or new lines are removed. This ensures that the text is clean and well-structured for further processing.

### Embeddings and Search Index:
The project utilizes Cohere for generating embeddings (vectors) from the input texts. These embeddings are then used to build a search index using the Annoy library. The search index enables efficient retrieval of relevant articles based on the similarity of their embeddings to the query.

### Searching Articles:
The system is designed to search for articles related to the user's query within the text archive. This involves retrieving the nearest neighbors from the search index, which represents the most relevant articles based on the similarity of their embeddings to the query.

### Generating Answers:
The final step is generating answers to user queries. The system extracts the top result from the search and uses it as context. A prompt is then constructed, including the context and the user's question. This prompt is fed into Cohere's generative model, which produces intelligent and context-aware answers to the user's query.

## Implementation

To run the AI Article Assistant, follow these steps:

1. **Set Up a Python Virtual Environment**: This isolates your project dependencies from other Python projects.
   ```bash
   python3 -m venv venv
   . venv/bin/activate
   ```

2. **Install Required Dependencies**: Ensure all necessary libraries are installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**: Execute the main script to start the tool.
   ```bash
   python3 app.py
   ```

## Output

![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/cd7b82bc-167f-4f6d-a9f3-a5347218fa39)


[Google Slides(AI Article Assitant)](https://docs.google.com/presentation/d/1-uLn_G1VYqCMl8tqd_qax9Dz33pGBzqe3xXBD_A9eWI/edit?usp=sharing)
