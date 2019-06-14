import sys

from read_keywords import load_keywords
from googlenews_search import search_data
from save_data import save


def main(filename):
    if not filename:
        raise Exception('The keywords filename is required!')

    # load keywords
    keywords = load_keywords(filename)
    # read data
    
    results = search_data(keywords)

    # save data
    save(results)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        main(filename)
    else:
        raise Exception('The filename parameter is required!')
