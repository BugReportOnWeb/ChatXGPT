from dotenv import load_dotenv
import openai

import json
import os
import random

load_dotenv()
KEY = os.getenv("OPENAI_API_KEY")

with open("../data/intents.json") as intent_file:
    data = json.load(intent_file)

tag_pattern_set = ""
ignored_characters = [".", ",", "?", "*", "/", "#", "@", "!"]

for intent in data["intents"]:
    index = 0

    while index < len(intent["patterns"]):
        if intent["patterns"][index] not in ignored_characters:
            tag = intent["tag"]
            pattern = intent["patterns"][index]
            tag_pattern_set += tag + " -> " + pattern + ", "
            break
        else:
            index += 1;


tag_pattern_set = tag_pattern_set.strip()[:-2]

def gpt(user_prompt):
    openai.api_key = KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text


def chat(user_input):
    while True:
        # For Debugging on terminal
        # user_input = input("You: ") 
        user_input = user_input.strip()
        if user_input.lower() == "quit":
            break

        tag_define_prompt = f"Choose/Guess the tag from the '<tag> -> <pattern>' set ({tag_pattern_set})"
        ans_define_prompt = f"for the user input: '{user_input}'"
        tag = gpt(f"{tag_define_prompt} {ans_define_prompt}").strip()

        for intent in data["intents"]:
            if tag == intent["tag"]:
                response =  random.choice(intent["responses"])

        return response

