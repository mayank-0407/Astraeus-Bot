# https://newsapi.org/
import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv('env_news_api_key')

def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    # print(articles)
    return articles
