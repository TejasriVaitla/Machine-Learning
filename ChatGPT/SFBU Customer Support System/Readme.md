# SFBU Customer Support System

## Project Description

This project focuses on the implementation of the SFBU (San Francisco Bay University) Customer Support System using text-based interactions. The system leverages advanced technologies like Vectorstores, Embedding, and Retrieval Augmented Generation (RAG) to provide efficient support services to SFBU stakeholders.

## Prerequisite

Before diving into the project implementation, it's essential to understand the following concepts and tools:

- **Vectorstores:** A technology for document embedding and similarity search.
- **Embedding:** Techniques for converting text data into numerical representations.

## Design

The project implementation involves several key steps, as outlined below:

### Step 1: Overview of the Workflow for RAG

This step provides an overview of the entire workflow, introducing the fundamental concepts and processes.

### Step 2: Load Document and Create VectorDB

Here, we load relevant documents and create a VectorDB, which allows for efficient document handling and similarity search.

### Step 3: Similarity Search to Select Relevant Chunks (Splits)

We perform similarity searches to select relevant document chunks (splits) based on user queries.

### Step 4: Create Language Model (LLM)

Creating a Language Model (LLM) is a pivotal step to generate responses and answer user queries.

### Step 5: RetrievalQA Chain (Optional)

This optional step involves creating a RetrievalQA Chain, which enhances question-answering capabilities.

- **Step 5.1:** Create a Prompt Template
- **Step 5.2:** Create QA Chain Prompt from the Prompt Template
- **Step 5.3:** Run QA Chain from the "QA Chain Prompt" using the "Stuff" chain type

### Step 6: Conversational Retrieval Chain

This step focuses on building a Conversational Retrieval Chain to facilitate interactive conversations.

- **Step 6.1:** Create Memory
- **Step 6.2:** QA with Conversational Retrieval Chain
- **Step 6.3:** Test Conversational Retrieval Chain

- **Step 6.3.1:** First Question
- **Step 6.3.2:** Follow-up Question

### Step 7: Create a Chatbot that Works on Your Documents

This final step involves the creation of a chatbot that interacts with your documents, enhancing user engagement.

- **Step 7.1:** Create Business Logic
- **Step 7.2:** Create a Web-Based User Interface

In this step, you have the option to modify the chatbot GUI to create a web-based user interface, allowing users to interact seamlessly.

## Implementation

To run the Chatbot project on Ubuntu, follow these steps:

1. Create a Python virtual environment:
   ```
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```
   . venv/bin/activate
   ```

3. Install the required dependencies from the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

4. Start the application by running `chat.py`:
   ```
   python3 chat.py
   ```
![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/03d4714b-2624-4273-826d-bd99b9171b6c)
   
## Output

![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/c0287e4c-d188-49ac-8ee5-7febd47cf272)


