# https://jokeapi.dev/
import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()
    if "joke" in data:
        return data["joke"]
    return "No joke found."
