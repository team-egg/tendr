import requests
from bs4 import BeautifulSoup as BS
import urllib.request as req
import re

def google_news(topic):
    """function to search keyword from google news, and return the first 20 matching links in a list"""

    google_url = f'https://news.google.com/rss/search?hl=en-US&gl=US&ceid=US:en&q={topic}'

    source = req.urlopen(google_url).read()
    soup = BS(source, 'xml')
    items = soup.find_all('item')
    links = []
    for i in range(len(items)):
        title = items[i].find('title')
    
        if re.search(topic, title.text, re.IGNORECASE):
            
            link = items[i].find('link')
            links.append(link.text)

        if len(links) >20:
            break

    return links
   


if __name__ == "__main__":
    
    print(google_news('tesla'))