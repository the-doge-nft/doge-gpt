
import os

import openai
from flask import Flask, request
from flask_cors import CORS

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/health', methods=["GET"])
def get_health():
    return {"status": "bork"}

@app.route('/prompt', methods=["POST"])
def hello_world():
    prompt = request.json.get("prompt")
    generated_prompt = get_doge_prompt(prompt)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generated_prompt,
        temperature=0.6,
        max_tokens=2048,
    )
    text = response["choices"][0]["text"]
    return {"data": text}


@app.route('/list-models')
def list_models():
    response = openai.Engine.list()
    return response


def get_doge_prompt(prompt):
    return f"{prompt} in the style of doge using words such as wow, such, much, very, and amaze"
