import requests
from decouple import config
from spreadsheets import save_from_api as save


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
        
        save(key, response_json)
