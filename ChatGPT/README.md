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

### Web-Based (Python Flask)
The web-based implementation utilizes the Flask framework to offer a user-friendly interface for interacting with the system. Users can access the system via a web browser, making it user-friendly and accessible. This web interface enables users to input questions and obtain responses, enhancing the overall user experience and accessibility of the system.

## Implementation (Command Line Based & Web Based)

Step 1.1.1. Execute the complete code on Jupyter Notebook (`command_code.ipynb`) or Google Colab.

### Ubuntu Terminal Setup
To run this project on an Ubuntu system, follow these steps:


1. Export the Jupyter notebook (from step 1.1.1) to a .py file and split it into separate parts (`crawl.py`, `embed.py`, `app.py`).

2. Install Python 3.10's virtual environment package, if not already installed:

 ```bash
  $ sudo apt install python3.10-venv
  ```
* Create a Python virtual environment named 'venv'
```bash
$ python3 -m venv venv
```
* Activate the virtual environment
```bash
$ . venv/bin/activate
```
* Install the required Python packages listed in 'requirements.txt'
```bash
$ pip install -r requirements.txt
```

* To crawl data from webpages, run:
```bash
$ python3 crawl.py
```
* To embed the crawled data, run:
```bash
$ python3 embed.py
```
* To run the system, run:
```bash
$ python3 app.py
```
* To deactivate the virtual environment, run:
```bash
$ deactivate
```

## Output

* Command Line Based

  ![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/3e0eea64-5afb-4caa-99eb-ef526251b477)

* Web Based

  ![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/cc1fbe67-2f99-445c-8d73-a9efe8bc7f69)

  ![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/cb5f5d46-e766-42a4-98e5-6058fda58525)

  ![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/e2beea85-aff7-4741-90b6-78aee85280eb)

  ![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/1653864c-79d1-4d57-8612-9b8bf60bfe91)


### Customer Support System Using ChatGPT (Google Slides)

[Customer Support System(Slides)](https://docs.google.com/presentation/d/1owShXzGYxCsduLe9XTfHx8StQ7d0srAtT2oZMkLhd6s/edit?usp=sharing)
