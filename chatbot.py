import openai
import json
from flask import Flask, render_template, request
from dotenv import dotenv_values

config = dotenv_values('.env')
openai.api_key=config["API_KEY"]


messages = []
while True:
    try:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        messages.append(res["choices"][0]["message"].to_dict())
        print("Assistant:", res["choices"][0]["message"]["content"])
 

    except KeyboardInterrupt:
        print("Exiting...")
        break

print(res)