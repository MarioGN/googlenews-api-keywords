import sys
from decouple import config
from keywords import load_keywords
from google_api_search import search_data as api_search_data
from spreadsheets import init_outputfile


KEYWORDS_FILE = config('KEYWORDS_FILE', default='keywords.xlsx')
OUTPUT_FILE = config('OUTPUT_FILE', default='output.xls')

# google api key
SECRET_KEY = config('SECRET_KEY')
# number of results by keyword
RESULT_NUMBER = config('RESULT_NUMBER', default='80', cast=int)


def main():
    # load keywords list form .xlsx file      
    keywords = load_keywords(KEYWORDS_FILE)

    # init result file
    init_outputfile(OUTPUT_FILE)

    # search results and save
    api_search_data(keywords, SECRET_KEY, RESULT_NUMBER)


if __name__ == "__main__":
    main()
