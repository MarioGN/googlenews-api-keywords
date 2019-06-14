import sys

from read_keywords import load_keywords
from google_api_search import search_data as api_search_data
from spreadsheets import init_outputfile


def main(filename):
    if not filename:
        raise Exception('The keywords filename is required!')
        
    init_outputfile()
    keywords = load_keywords(filename)
    api_search_data(keywords)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        raise Exception('The filename parameter is required!')