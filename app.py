from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def chatbot_response(user_input):
    # Simple logic for the chatbot response
    app_title = os.environ.get("APP_TITLE", "ChatBot")     
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!"
    }
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.") + " from " + app_title

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