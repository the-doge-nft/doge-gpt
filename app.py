
import os

import openai
from flask import Flask

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=get_prompt(),
        temperature=0.6,
    )
    text = response["choices"][0]["text"]
    print(response)
    return {"response": response, "text": text, "prompt": get_prompt()}


@app.route('/list-models')
def list_models():
    response = openai.Engine.list()
    return response


def get_prompt():
    return "what is my name in the style of doge"
