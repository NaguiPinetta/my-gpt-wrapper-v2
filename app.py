import openai
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = query_gpt(user_input)
        return render_template("index.html", user_input=user_input, response=response)
    return render_template("index.html", user_input=None, response=None)

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
    app.run(debug=True)

