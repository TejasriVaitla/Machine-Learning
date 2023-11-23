# Keyword and Semantic Searches with ReRank

## Introduction

This project is focused on implementing an advanced search and reranking system. It leverages the capabilities of Cohere and Weaviate to perform dense retrieval and rerank search results, enhancing the relevance and accuracy of information retrieval. This system can be applied in various domains where precise and context-aware search results are essential.

## Design

Dense Retrieval:
The project begins with Dense Retrieval, utilizing Weaviate to retrieve documents relevant to the user's query. This phase focuses on the semantic understanding of the query to identify documents that match the user's intent.

Keyword Search and ReRank:
Following Dense Retrieval, the project employs a keyword search mechanism using Weaviate. The initial search yields a set of results, which are then subjected to ReRanking using Cohere's ReRank models. This step further refines the order of results, enhancing the overall quality of the responses.

## Implementation

To get the system up and running, follow these steps:

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
   python3 rerank.py
   ```


## Output

Please find the output of the model is in output.txt

![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/5e47f604-6c75-4da4-b259-570f238942ff)

[Google Slides(ReRank)](https://docs.google.com/presentation/d/1Y12HDsetaphURCSZvQs5bHsHqXWH68LT4bYvCUGorYE/edit?usp=sharing)

