import os
import openai
from flask import Flask, request, jsonify

# Set your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Ensure that the API key is loaded correctly (this will print it in the console for debugging purposes)
print(f"API Key Loaded in Flask: {openai.api_key}")

# Initialize Flask app
app = Flask(__name__)

@app.route('/ask-dance-question', methods=['POST'])
def ask_dance_question():
    data = request.get_json()
    sender_id = data.get('sender_id')
    user_query = data.get('message')

    try:
        # OpenAI API call using the correct format
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4" if needed
            messages=[
                {"role": "system", "content": "You are a dance training assistant for The Dance Process."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=300
        )

        reply = response.choices[0].message['content']

        return jsonify({"sender_id": sender_id, "response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)

