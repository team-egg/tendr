# Project : Tendr

## Team Egg : 
- [Peng Chen](https://github.com/PengChen11)
- [Eugene Monnier](https://github.com/eugenemonnier)
- [H Griffin](https://github.com/h-griffin)

# project management tools : 
- [Team Trello Board](https://trello.com/b/bvFTbjz2/tendr)

# description:
tendr predicts public opinion on stock companies. search the stock tag and this app will find the company that owns it and current public opinion on that company. 

# links and rescources:
- [how to scrape google with python](https://hackernoon.com/how-to-scrape-google-with-python-bo7d2tal)
- [custom search JSON API](https://developers.google.com/custom-search/v1/overview)
- [yahoo finance API](https://finance.yahoo.com/quote/{stock_id})
- [microsoft article for API test](https://www.investopedia.com/microsoft-stock-pops-above-its-monthly-risky-level-4844946)



# whiteboard
![whiteboard image 1](/assets/whiteboard-1.png)

### project plan: 
start in jupyterlab
import funtion module
call function module with **stock id**
call google search of **key**
find 10 articles of *company*
run articles through api
get score

stretch
save data to new file
display

## function descriptions:
### company name:
- take input form user
- google search API 
    - [yahoo finance URL](https://finance.yahoo.com/quote/{stock_id})
         - ```import requests
            def get_symbol(symbol):
                url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

                result = requests.get(url).json()

                for x in result['ResultSet']['Result']:
                    if x['symbol'] == symbol:
                        return x['name']

                company = get_symbol("MSFT")

                print(company)```
    - [google search JSON API](https://developers.google.com/custom-search/v1/overview)
- scrape page for 10 articles
    - save article results to text file
- **output** : article in text file 

- give text file to api 

### article grade:
- take input from user
- insert into [microsoft sentiment API /text analytics]
    - receive 1-100 % score of 
- **output** :
    if between -val and -val
    print string

