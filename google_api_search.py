from pprint import pprint
import requests

from decouple import config
from save_data import save_api


SECRET_KEY = config('SECRET_KEY')
url = 'https://newsapi.org/v2/everything?'

def search_data(keywords):
    for key in keywords:
        parameters = {
            'q': key, 
            'pageSize': 5,  
            'apiKey': SECRET_KEY 
        }

        response = requests.get(url, params=parameters)
        response_json = response.json()
        # return response_json
        save_api(key, response_json)

