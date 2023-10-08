# Customer Support System: An email to the customer

## Introduction

The Customer Support System is a web application that utilizes the OpenAI GPT-3.5 Turbo model to provide customer support for an electronic product company. This system generates customer comments, email subjects, comment summaries, and email responses based on user interactions. It offers support in multiple languages, including English, Spanish, and Portuguese.

## Design

The system is designed as a Flask web application with a straightforward user interface. Users can select the language in which they want to generate email responses and view the generated customer comment and email response. The application follows these key design components:

- **Flask Web Application**: The application is built using Flask, a lightweight web framework in Python, to handle user interactions.

- **OpenAI Integration**: It integrates with the OpenAI GPT-3.5 Turbo model to generate text-based responses for customer support tasks.

- **HTML Template**: The user interface is designed using an HTML template (`index.html`) with a language dropdown menu, question, and answer containers.


<table border="1" cellpadding="10">
        <thead>
            <tr>
                <th>Step</th>
                <th>Description</th>
                <th>Input to ChatGPT</th>
                <th>ChatGPT's Response</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> 1</td>
                <td>Generate Customer's Comment</td>
                <td>Detailed product descriptions</td>
                <td>A 100-word comment about the products</td>
            </tr>
            <tr>
                <td> 2</td>
                <td>Generate Email Subject</td>
                <td>Customer's comment from Step 1</td>
                <td>Email subject inferred from the customer's comment</td>
            </tr>
            <tr>
                <td> 3</td>
                <td>Generate Comment Summary</td>
                <td>Customer's comment from Step 1, Customer's selected language</td>
                <td>
                    <strong>3.1:</strong> Summary in English using Summarization<br>
                    <strong>3.2:</strong> Translation to the selected language
                </td>
            </tr>
            <tr>
                <td> 4</td>
                <td>Analyze Customer Comment Sentiment</td>
                <td>Customer's comment from Step 1</td>
                <td>Sentiment analysis (Positive/Negative)</td>
            </tr>
            <tr>
                <td> 5</td>
                <td>Generate Customer Email</td>
                <td>
                    Customer's comment from Step 1<br>
                    Comment summary from Step 3.2<br>
                    Sentiment result
                </td>
                <td>An email response to the customer</td>
            </tr>
        </tbody>
    </table>
    
We will test the following:

<img src="https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/065fd3ed-888f-446b-acfe-e179174f4ad4">

## Implementation

To run this application, follow these implementation steps:

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   . venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install flask openai python-dotenv
   ```

4. Start the Flask application:
   ```bash
   python3 app.py
   ```

## Test (Output)

* Open http://127.0.0.1:5000 to see the result


Test Case 1: English to English

![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/276ff739-dfcd-47d6-ab2b-552926cd27dc)

Test Case 2: English to Polish(Non-English)

![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/2d66a003-f150-44ea-8e82-a32cee6173b7)

Test Case 3: Non-English(French) to English

![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/9c17cb1d-f574-4874-a903-ff41f4ea7265)

Test Case 4: Non-English(French) to Non-English(French)

![image](https://github.com/TejasriVaitla/Machine-Learning/assets/128747986/172c217d-6b27-425c-891f-e4f041e0d654)


### Customer Support System: An email to the customer (Google Slides)

[Customer Support System(Slides)](https://docs.google.com/presentation/d/1-9xlAwnhfQLiNNr-Ek1cnjSYo5KUit71K7PJrcImTtc/edit?usp=sharing)
