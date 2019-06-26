from random import randint
from time import sleep
from GoogleNews import GoogleNews
from spreadsheets import save_from_lib as save


def search_data(keywords):
    googlenews = GoogleNews()
    results = {}

    for key in keywords:
        googlenews.search(key)  
        key_result = []

        while len(googlenews.results) < 10:
            googlenews.getpage(2)
            sleep(randint(1,3))

        print('lib search...')
        results[key] = googlenews.results

    save(results)
