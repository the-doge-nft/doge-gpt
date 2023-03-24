
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
    print(response)
    return response.choices[0].text


def get_prompt():
    return "what is my name in the style of doge"
