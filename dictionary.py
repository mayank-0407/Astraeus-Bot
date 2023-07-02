# https://rapidapi.com/community/api/urban-dictionary
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_urban_dictionary_definition(term):
    url = f"https://mashape-community-urban-dictionary.p.rapidapi.com/define?term={term}"
    headers = {
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
        "X-RapidAPI-Key": os.getenv('env_X_RapidAPI_Key')
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if "list" in data:
        if data["list"]:
            definition = data["list"][0]["definition"]
            example = data["list"][0]["example"]
            return f"**Definition:** {definition}\n\n**Example:** {example}"
    return "No definition found."
