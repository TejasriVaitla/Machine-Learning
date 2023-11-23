# AI-Driven Drug-Malady Classification System

## Introduction
The aim of this project is to convert an XLSX data file containing drug and malady information into a JSONL format suitable for fine-tuning a model using Pandas and OpenAI tools. The data is transformed into a specific format, ensuring proper tokenization and classification. This project focuses on preparing the data for a medical model by creating prompts and completions in the desired structure.

## Design
The data preparation process involves using Pandas to read the XLSX file, transforming the drug and malady information, and exporting it into a JSONL file. The desired format for each entry in the JSONL file is {"prompt": "Drug: <DRUG NAME>\nMalady:", "completion": " <MALADY NAME>"}. Additionally, a unique identifier is assigned to each malady, eliminating the need for a stop sequence at the end of each completion.

The provided Python script utilizes Pandas to read the data, create prompts and completions, and write the results into a JSONL file. The subsequent steps involve using OpenAI tools for data analysis, splitting the data into training and validation sets, and fine-tuning a model for classification. The OpenAI CLI commands guide the user through the process, including exporting the API key, preparing the data, training the model, checking job progress, and completing the fine-tuning.

## Implementation
To implement this project, follow these steps:

1. **Set up the Python Environment**:
   ```bash
   python3 -m venv venv
   . venv/bin/activate
   pip install pandas openpyxl openai==0.28
   ```

2. **Process the Dataset**:
   - Run the `app.py` script to process the Excel dataset and to create a jsonl file.
     ```bash
     python3 app.py
     ```

3. **Prepare Data for Fine-Tuning**:
   - Use the OpenAI CLI to prepare the data for fine-tuning.
     ```bash
     openai tools fine_tunes.prepare_data -f drug_malady_data.jsonl
     ```

4. **Set Up OpenAI API Key**:
   - Export your OpenAI API key.
     ```bash
     export OPENAI_API_KEY="your_api_key_here"
     ```

5. **Fine-Tune the Model**:
   - Create a fine-tuning job using the OpenAI API.
     ```bash
     openai api fine_tunes.create \
        -t "drug_malady_data_prepared_train.jsonl" \
        -v "drug_malady_data_prepared_valid.jsonl" \
        --compute_classification_metrics \
        --classification_n_classes 7 \
        -m ada \
        --suffix "drug_malady_data"
     ```

    ![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/b4249dac-7c9c-44ad-9aa8-140832dfb570)

6. **Follow the Fine-Tuning Job**:
   - Monitor the fine-tuning job using the job ID.
     ```bash
     openai api fine_tunes.follow -i <JOB ID>
     ```

     ![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/83e4c664-87ad-4361-8566-15b008496064)

7. **Run the Test Script**:
   - Execute `test.py` to classify drugs using the fine-tuned model.
     ```bash
     python3 test.py
     ```
## Output
![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/0cc9ca1b-4d49-4c87-9072-64cf53e33757)

[Google Slides (Fine-Tuning)](https://docs.google.com/presentation/d/1Uf688hlOOnFp6E8SfHTRP_Tdh-CVya5diRQCv13dlGc/edit?usp=sharing)
