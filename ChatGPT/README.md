# Customer Support System using ChatGPT

## Introduction
This project aims to create a Customer Support System that utilizes web crawling, text embedding, and the OpenAI API to provide answers to questions based on webpage content. It includes two implementations: `Command Line Based` and `Web Based`.

## Design
The system is designed to perform the following steps:

**1. Web Crawling:**  
   It scans webpages, extracts their text content, and stores it for future processing.

**2. Text Embedding:**  
   The extracted text is tokenized and transformed into numerical representations using OpenAI's embedding models.

**3. Question Answering:**  
   Users can inquire about the crawled webpages, and the system generates responses by employing the embeddings and OpenAI's API.

### Command Line Based
In the command line-based implementation, users interact with the system via the Ubuntu terminal. They can ask questions about the webpages crawled by the system, and the system generates responses based on the embedded text data. This implementation offers a straightforward and text-based interface for users to access web content.

### Web-Based (Flask)
The web-based implementation utilizes the Flask framework to offer a user-friendly interface for interacting with the system. Users can access the system via a web browser, making it user-friendly and accessible. This web interface enables users to input questions and obtain responses, enhancing the overall user experience and accessibility of the system.

## Implementation (Command Line Based & Web Based)

### Ubuntu Terminal Setup
To run this project on an Ubuntu system, follow these steps:

1. Execute the complete code on Jupyter Notebook (`command_code.ipynb`) or Google Colab.

2. Export the Jupyter notebook to a .py file and split it into separate parts (`crawl.py`, `embed.py`, `app.py`).

3. Install Python 3.10's virtual environment package, if not already installed:

   ```bash
   $ sudo apt install python3.10-venv
   
