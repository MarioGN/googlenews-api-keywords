# Google News API search keywords

## How to use?

1. Clone or download the repository.
2. Create a virtualenv with Python3.7
3. Activate virtualenv
4. Install the dependencies
5. Configure .env file
6. Place the keyword file in the folde
7. Configure API key
8. Run the script.

```console
git clone git@github.com:MarioGN/googlenews-scrap.git google
cd google
virtualenv -p python3.7 venv
source venv/bin/activate
pip install -r requirements.txt
cp env-sample .env
# place the keywords file
# configure API KEY
python main.py
```