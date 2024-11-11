from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def chatbot_response(user_input):
    # Simple logic for the chatbot response
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!"
    }
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3050))
    app.run(debug=True, port=port)