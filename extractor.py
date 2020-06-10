import requests
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("token")

def extractor(news_url):
    """function to send news url to extraction api to extract text from the articale and return as string"""

    url = f'https://api.diffbot.com/v3/article?token={SECRET_KEY}&url={news_url}'

    response = requests.get(url)

    data = response.json()

    text = data["objects"][0]['text']

    return text

# if __name__ == "__main__":
    
