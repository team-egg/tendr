import requests
from bs4 import BeautifulSoup as BS
import urllib.request as req
import re
from alive_progress import alive_bar 

def google_news(topic):
    """function to search keyword from google news, and return the first 20 matching links in a list"""
    keyword = topic.replace(' ', '%20')
    google_url = f'https://news.google.com/rss/search?hl=en-US&gl=US&ceid=US:en&q={keyword}'

    source = req.urlopen(google_url).read()
    soup = BS(source, 'xml')
    items = soup.find_all('item')
    links = []
    for i in range(len(items)):
        if len(links) >= 20:
            break
        title = items[i].find('title')

        topic_parse = topic.split(' ')
        if re.search(topic_parse[0], title.text, re.IGNORECASE):
            
            link = items[i].find('link')
            links.append(link.text)
            
    return links