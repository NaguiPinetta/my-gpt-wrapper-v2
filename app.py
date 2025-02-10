import openai
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS  # Import CORS

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_json()  # Get JSON data properly
        user_input = data.get("user_input", "")  # Extract user input safely
        response = query_gpt(user_input)
        return jsonify({"response": response})  # Return JSON

    return jsonify({"message": "Welcome to the GPT Wrapper API"})

def query_gpt(prompt):
    try:
        client = openai.OpenAI()  # Initialize OpenAI Client
        response = client.chat.completions.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Ensure Flask runs on all interfaces
