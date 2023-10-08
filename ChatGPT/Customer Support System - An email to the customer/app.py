# 1. Initialization and imports
import openai
import os
from flask import Flask, render_template, request
# Import products_description from products_data.py
from products_data_french import products_data_french as products_data

with open(".env") as env:
    for line in env:
        key, value = line.strip().split("=")
        os.environ[key] = value

# Initializing the API key and organization id
openai.api_key = os.environ.get("API_KEY")
openai.organization = os.environ.get("ORG_ID")


app = Flask(__name__, static_url_path='/static')

def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

# Step 1: Generate a Customer's Comment
def generate_customer_comment(products_data):
    prompt = f"""
    Supposez que vous êtes un client d'une entreprise de produits électroniques.
    Écrivez un commentaire de 100 mots seulement sur les produits, délimité par des triples backticks, dans leur propre langue. 
    Produits : ```{products_data}```
    """
    response = get_completion(prompt)
    return response



# Step 2: Generate Email Subject
def generate_email_subject(comment):
    prompt = f"""
    En supposant que vous fournissiez un support client pour une entreprise de produits électroniques.
    Sur la base du commentaire du client délimité par des triples backticks, suggérez un objet d'e-mail court pour répondre au client. 
    Commentaire : ```{comment}```
    """
    response=get_completion(prompt)
    return response

# Step 3: Generate Customer Comment Summary
def summarize_comment(comment):
    prompt = f"""
    En supposant que vous fournissiez un support client pour une entreprise de produits électroniques.
    Fournissez un résumé concis en 50 mots du commentaire du client suivant, délimité par des triples backticks. Commentaire : ```{comment}```
    """
    response=get_completion(prompt)
    return response

def translate_summary_with_chatgpt(language, summary):
    prompt = f"""
    Traduisez le résumé suivant délimité par des triples backticks vers la langue délimitée par <>. 
    Langue : ```{language}```   
    Résumé : <{summary}>
    """
    response=get_completion(prompt)
    return response

# Step 4: Analyze Customer Comment Sentiment
def analyze_sentiment(comment):
    prompt = f"""
    En supposant que vous fournissiez un support client pour une entreprise de produits électroniques.
    Quel est le sentiment du commentaire délimité par des triples backticks ? Est-ce positif ou négatif ? 
    Commentaire : ```{comment}```
    """
    max_tokens = 10
    response = get_completion(prompt)
    sentiment = response.lower()
    if "positif" in sentiment:
        return "positif"
    elif "négatif" in sentiment:
        return "négatif"
    else:
        return "neutre"

# Step 5: Generate Customer Email
def generate_customer_email(summary, sentiment, email_subject, language):
    if sentiment == "positif":
        response_text = "Nous sommes ravis d'entendre vos commentaires positifs et apprécions vos paroles encourageantes. Votre satisfaction est notre priorité absolue !"
    elif sentiment == "négatif":
        response_text = "Nous sommes vraiment désolés d'apprendre votre expérience. Vos commentaires sont essentiels, et nous nous efforcerons de répondre à vos préoccupations."
    else:
        response_text = "Merci pour vos commentaires ! Nous cherchons toujours à nous améliorer, et vos idées sont précieuses."
    prompt = f"""
    En supposant que vous fournissiez un support client pour une entreprise de produits électroniques.
    Étant donné les paramètres spécifiés ci-dessous :
    - Résumé du commentaire délimité par des backticks (`{summary}`)
    - Notre texte de réponse délimité par des triples guillemets (\"\"\"{response_text}\"\"\")
    - Traduisez l'objet de l'e-mail délimité par des chevrons ({email_subject}) en langue "{language}"
    Écrivez un e-mail complet en réponse au commentaire du client en utilisant la langue "{language}".
    """
    response = get_completion(prompt)
    return response


@app.route('/', methods=['GET', 'POST'])

def index():
    answer = ""
    comment = generate_customer_comment(products_data)
    print("A customer comment has been generated.")
    if request.method == 'POST':
        language = request.form.get('language')  # Fetch language input from the webpage
        print(f"Selected language: {language}")
        answer = process_comment_to_email(comment, language)
    return render_template('index.html', question=comment, answer=answer)

def process_comment_to_email(comment, language):
    # Step 2: Generate Email Subject
    email_subject = generate_email_subject(comment)
    print(f"An email subject is generated from the customer's comment.")
    # Step 3: Generate Customer Comment Summary
    summary = summarize_comment(comment)
    print("A Summary is generated from the customer comment.")
    translated_summary = translate_summary_with_chatgpt(language, summary)
    print("The summary has been translated to requested language.")
    # Step 4: Analyze Customer Comment Sentiment
    comment_sentiment = analyze_sentiment(comment)
    print(f"Sentiment of the comment is detected as: {comment_sentiment}")
    # Step 5: Generate Customer Email
    email_content = generate_customer_email(translated_summary, comment_sentiment, email_subject, language)
    print("A customer email has been generated.")
    return email_content


if __name__ == '__main__':
    app.run(debug=True)