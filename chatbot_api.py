from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "Hello, this is your chatbot API!"

@app.route("/ask", methods=["POST"])
def ask_dance_question():
    data = request.get_json()
    sender_id = data.get("sender_id")
    user_query = data.get("message")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a dance training assistant for The Dance Process."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=300
        )

        reply = response["choices"][0]["message"]["content"]
        return jsonify({"sender_id": sender_id, "response": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

