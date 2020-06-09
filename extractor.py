import requests

def extractor(news_url):
    """function to send news url to extraction api to extract text from the articale and return as string"""

    url = f'https://api.diffbot.com/v3/article?token=5e33cba706016a35ba1b1acc0dd8c20f&url={news_url}'

    response = requests.get(url)

    data = response.json()

    text = data["objects"][0]['text']

    return text

if __name__ == "__main__":
    print(extractor('https://cleantechnica.com/2020/06/09/dispatches-from-the-front-line-on-teslas-roadrunner-project/'))
