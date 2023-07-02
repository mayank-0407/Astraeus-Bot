# https://developers.giphy.com/dashboard/
import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$', intents=intents)
giphy_api_key = os.getenv('env_giphy_api_key')

def get_random_gif():
    url = f"https://api.giphy.com/v1/gifs/random?api_key={giphy_api_key}"
    response = requests.get(url)
    data = response.json()
    gif_url = data["data"]["images"]["original"]["url"]
    return gif_url
