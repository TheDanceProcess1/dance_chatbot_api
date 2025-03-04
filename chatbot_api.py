from flask import Flask, request, jsonify
import openai
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Firebase credentials from environment variable
firebase_service_account = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")
if firebase_service_account:
    cred = credentials.Certificate(eval(firebase_service_account))
    firebase_admin.initialize_app(cred)
    db = firestore.client()
else:
    raise ValueError("Missing Firebase Service Account Key")

# Root Route - Health Check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Chatbot API is running!"})

# Chat Route - Processes User Messages
@app.route("/chat", methods=["POST"])
def chat():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )

        bot_reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask App
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000
    app.run(host="0.0.0.0", port=port, debug=True)
