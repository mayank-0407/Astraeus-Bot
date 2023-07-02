# pip install python-dotenv
# py -3 -m pip install -U discord.py
# pip install youtube_dl
# pip install requests
# pip install google-api-python-client
# pip install pyowm
# pip install ffmpeg-python
import discord
import requests
import json
from yt import *
from weather import *
from giphy import *
from news import *
from dictionary import *
from joke import *
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents().all() 
client = discord.Client(intents=intents)

appreciate=['thanks','Thanks','WellDone','well done']

def get_quotes():
    response=requests.get('https://zenquotes.io/api/random')
    json_data=json.loads(response.text)
    quote=json_data[0]['q']+"-"+json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('Successfully connected')

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith('$about'):
        await message.channel.send("**Welcome to Astraeus**, your trusty companion in the digital realm! Astraeus is a versatile and feature-rich bot designed to enhance your Discord experience. From entertainment to utility, Astraeus is here to make your server more engaging and enjoyable.\n**Features and Capabilities** \n Music Playback: Enjoy high-quality music streaming in your voice channels.\nModeration Tools: Keep your server in check with powerful moderation features.\n Fun and Games: Engage with your community through various fun games and activities. \n Information and Utilities: Access helpful information and utility commands at your fingertips. \n Customization: Personalize Astraeus with configurable settings to suit your server's needs.")

    if message.content.startswith('$hello'):
        await message.channel.send('Hey! How can I make your day better?')

    if message.content.startswith('$hi'):
        await message.channel.send("Hi! I'm at your service. How can I assist you?")

    if message.content.startswith('$Hi'):
        await message.channel.send("Hello! Welcome to our server. How can I assist you?")

    if message.content.startswith('$help'):
        all_comm="Make Sure to use '$' before typing any command.\n **$inspire** : This command generates and displays an inspirational quote or message. It provides users with a dose of motivation or inspiration to brighten their day.\n **$yt (context) $join $play $resume $stop $skip** : The $yt command allows users to search for YouTube videos based on a given context or topic. It returns relevant videos matching the provided context, allowing users to easily find and share videos within the Discord server.\n**$weather (place)**: The $weather command provides users with current weather information for a specified location. Users can enter the name of a city, town, or any other location, and the bot will retrieve and display details such as temperature, humidity, wind speed, and conditions.\n**$gif**: The $gif command generates and displays a random animated GIF. It adds an element of fun and entertainment to the Discord server, allowing users to share amusing or expressive GIFs with each other.\n**$news (context)**: With the $news command, users can retrieve the latest news articles or headlines related to a specific context or topic. It fetches news from reliable sources and presents users with a brief summary and a link to the full article, keeping them informed and up to date.\n**$find (term)**: The $find command enables users to search for information or resources related to a given term. It can be used to look up definitions, Wikipedia articles, or any other relevant information, providing users with quick access to knowledge.\n**$joke**: The $joke command delivers a random joke or a series of jokes to lighten the mood and bring laughter to the Discord server. It adds a touch of humor and entertainment, creating a more enjoyable and engaging environment for users."
        await message.channel.send(all_comm)

    #quotes
    if message.content.startswith('$inspire'):
        quote=get_quotes()
        await message.channel.send(quote)

    if any(word in message.content for word in appreciate):
        await message.channel.send('Well This is my Job! But Thank You!')

    #Youtube
    if message.content.startswith('$yt'):
        search= message.content[6:].strip()
        try:
            await message.channel.send(get_videos(search[1]))
        except:
            await message.channel.send('Add the query about which you need video to search.')

    #Weather
    if message.content.startswith('$weather'):
        search= message.content[6:].strip()
        try:
            await message.channel.send(send_weather(search[1]))
        except:
            await message.channel.send('Add the place about which you need weather.')

    #Giphy
    if message.content.startswith('$gif'):
        await message.channel.send(get_random_gif())

    #News
    if message.content.startswith('$news'):
        data= message.content[6:].strip()  
        try:
            articles = get_news(data[1])
        except:
            await message.channel.send('Add the thing about which you need news.')
            
        for article in articles:
            title = article["title"]
            description = article["description"]
            url = article["url"]
            resp = f"**{title}**\n{description}\n{url}"
            await message.channel.send(resp)
            break

    #Dictionary
    if message.content.startswith('$find'):
        term= message.content[5:].strip()
        try:
            definition = get_urban_dictionary_definition(term)
            await message.channel.send(definition)
        except:
            await message.channel.send('Add the term about which you need find defination.')

    #Joke
    if message.content.startswith('$joke'):
        joke = get_joke()
        await message.channel.send(joke)


# client.run('MTEyNTA1ODg0Nzc3NDYxMzUwNA.G5xw12.sYUZsEqdljNdzPv-rihue9BFH8Igwan_WY36P4')
client.run(os.getenv('env_bot_token'))