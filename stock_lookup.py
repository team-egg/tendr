import re, requests
from bs4 import BeautifulSoup as bs

def stock_to_name():
  stock_id = input("Enter in the stock ID you'd like to look into: ")
  url = f'https://finance.yahoo.com/quote/{stock_id}'
  response = requests.get(url)
  soup = bs(response.content, 'html.parser')
  company_name = soup.find('h1', attrs={'data-reactid': 7})
  company_name = (company_name.text.strip()).replace(stock_id.upper() + ' - ','').replace(', Inc.', '')
  return company_name

# print(stock_to_name())