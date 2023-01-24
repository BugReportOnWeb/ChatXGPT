from dotenv import load_dotenv

import json
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

with open("./intents.json") as intent_file:
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

def chat(prompt):
    # Works with API
    # TODO
    return prompt


if __name__ == "__main__":
    user_input = input("You: ")
    user_input = user_input.strip()

    tag_define_prompt = f"Check for xyz ({tag_pattern_set})"
    ans_define_prompt = f"for the input {user_input}"

    print(f"{tag_define_prompt} {ans_define_prompt}")
    response = chat(f"{tag_define_prompt} {ans_define_prompt}")

    print(f"Bot: {response}")

