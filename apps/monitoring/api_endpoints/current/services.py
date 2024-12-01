import os

import requests
from dotenv import load_dotenv

load_dotenv()


def current_statistics(latitude, longitude):
    endpoint = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={os.getenv('API_KEY')}"
    response = requests.request("GET", url=endpoint).json()
    return response

