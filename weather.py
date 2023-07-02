# https://openweathermap.org/
import pyowm
import json
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('env_weather_api_key')
owm = pyowm.OWM(api_key)
mgr = owm.weather_manager()

def get_weather(location):
    observation = mgr.weather_at_place(location)
    weather = observation.weather
    return weather

def send_weather(location):
    weather = get_weather(location)
    temperature = weather.temperature('celsius')['temp']
    main_string="The current temperature in " + str(location) + " is :- " + str(temperature) + " °C . "
    return main_string