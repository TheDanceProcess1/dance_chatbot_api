from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, origins=["https://www.thedanceprocess.com", "https://chatbot-api.onrender.com"])

# Set OpenAI API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Hello, this is your chatbot API!"

@app.route("/ask", methods=["POST"])
def ask_dance_question():
    data = request.get_json()
    sender_id = data.get("sender_id")
    user_query = data.get("message")

    try:
        # OpenAI API call using the new format
        response = openai.chat.completions.create(
            model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a dance training assistant for The Dance Process."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=300
        )

        reply = response.choices[0].message.content

        return jsonify({"sender_id": sender_id, "response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

