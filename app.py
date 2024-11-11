from flask import Flask, render_template, request, jsonify
import os
from transformers import pipeline

app = Flask(__name__)

def chatbot_response(user_input):
    # Load the pre-trained model and tokenizer
    nlp = pipeline("text-generation", model="distilbert-base-uncased")

    # Generate a response
    response = nlp(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']

    # Add app title
    app_title = os.environ.get("APP_TITLE", "ChatBot")
    return response + " from " + app_title


@app.route("/")
def home():
    app_title = os.environ.get("APP_TITLE", "ChatBot") 
    return render_template("index.html", title=app_title)


@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3050))
    app.run(debug=True, host="0.0.0.0", port=port)