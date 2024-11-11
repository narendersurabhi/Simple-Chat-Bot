from flask import Flask, render_template, request, jsonify
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

app = Flask(__name__)

# Load the pre-trained LLaMA 2 13B model and tokenizer 
model_name = "meta-llama/LLaMA-2-13B-chat" 
tokenizer = AutoTokenizer.from_pretrained(model_name) 
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16)

# Set up the text generation pipeline 
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

def chatbot_response(user_input):
    # Load the pre-trained model and tokenizer
    nlp = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

    # Generate a response
    response = generator(user_input, max_length=150, num_return_sequences=1)[0]['generated_text']
    
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