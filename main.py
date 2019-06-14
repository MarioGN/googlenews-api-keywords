import sys
import pprint

from read_keywords import load_keywords
from googlenews_search import search_data as lib_search_data
from google_api_search import search_data as api_search_data
from save_data import save, save_api


def main(filename):
    if not filename:
        raise Exception('The keywords filename is required!')

    keywords = load_keywords(filename)
    results = api_search_data(keywords)
    # save(results)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        raise Exception('The filename parameter is required!')
