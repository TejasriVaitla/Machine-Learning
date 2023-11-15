# AI-based Alexa
## Introduction
This project integrates cutting-edge technologies in audio processing, speech recognition, conversational AI, and document context handling to create an advanced voice-activated conversational system. The system actively listens for a specific wake word, processes spoken queries or commands, and provides contextually relevant responses using information from a loaded document. This solution is particularly useful for interactive voice assistants, automated customer support, or educational tools where accessing document-based information through voice commands adds significant value.


## Implementation

### 1. Create a Python Virtual Environment:
```
python3 -m venv venv
. venv/bin/activate
```

### 2. Install Dependencies:
```
sudo apt update && sudo apt install ffmpeg
pip install -r requirements.txt
```

### 3. Run the application:
```
python3 app.py
```

    - The script will prompt you to enter a wake word. The default wake word is "hey computer".
    - Once the wake word is set, the script will begin listening for your voice commands.
    - To stop the script, press `Ctrl + C`.

## Output

