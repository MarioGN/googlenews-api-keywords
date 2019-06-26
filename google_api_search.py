import requests
from decouple import config
from spreadsheets import save


url = 'https://newsapi.org/v2/everything?'


def search_data(keywords, api_key, result_number):
    for key in keywords:
        print('keyword: {}...'.format(key))
        parameters = {
            'q': key, 
            'pageSize': result_number,  
            'apiKey': api_key, 
        }

        response = requests.get(url, params=parameters)
        response_json = response.json()
        
        save(key, response_json)
