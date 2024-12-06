import os

import requests
from dotenv import load_dotenv

load_dotenv()


def history_statistics(latitude, longitude, start, end):
    endpoint = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={latitude}&lon={longitude}&start={start}&end={end}&appid={os.getenv('API_KEY')}"
    response = requests.request("GET", url=endpoint).json()
    return response

