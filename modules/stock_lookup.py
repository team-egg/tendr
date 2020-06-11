import re, requests
from bs4 import BeautifulSoup as bs

def stock_to_name(stock_id):
  """takes in a stock id and returns the company name"""
  url = f'https://finance.yahoo.com/quote/{stock_id}'
  response = requests.get(url)
  soup = bs(response.content, 'html.parser')
  bad_stock_id = soup.find('span', attrs={'data-reactid': 6})
  if bad_stock_id.text == f"Symbols similar to '{stock_id.lower()}'":
    stock_id = input('Invalid stock ID. Please enter a valid stock ID: ')
    company_name = stock_to_name(stock_id)
  else:
    company_name = soup.find('h1', attrs={'data-reactid': 7})
    company_name = (company_name.text.strip()).replace(stock_id.upper() + ' - ','').split(', ')
  return company_name[0]
