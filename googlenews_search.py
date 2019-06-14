from random import randint
from time import sleep

from GoogleNews import GoogleNews


def search_data(keywords):
    googlenews = GoogleNews()
    results = {}

    for key in keywords:
        googlenews.search(key)  
        key_result = []

        while len(googlenews.results) < 20:
            googlenews.getpage(2)
            sleep(randint(1,10))

        results[key] = googlenews.results

    return results
