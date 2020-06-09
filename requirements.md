# whiteboard
![whiteboard image 1](/assets/whiteboard-1.png)
# project management tools : 
- [team GitHub project board](https://github.com/team-egg/tendr/projects/1?add_cards_query=is%3Aopen)

# vision
the vision of this project is to provide a new perspective on stock companies for a better look into how their stocks are doing. this project solves the assumption that a given companies stocks are down for poor quality product, when really the public may jsut be upset withthem, not actually afteting long term life of the stock. this product is important because it prevents the premptive loss of stock noto only for the owner, but for the company itself. 

# scope :
### in:
- this product will be in a python notebook
- this product will run get requests though apis to 
    - search the stock tag company owner
    - search articles about this company
    - score it on positive or negative rating
- it will display  data found in a data frame
- show what is trending in the data

### out:
- this product will not predict the stock markets
- this product will not be an android or IOS mobile app

# MVP :
- take a stock tag input from user
- search the stock tag company owner
    - display company name / info
- search articles about this company
    - display 10 recent articles found
- score it on positive or negative rating
    - display rating
- display comparison of all companies data together
- show what is trending
### stretch :
- view stock rise and fall compared to public perception

## usability:
to tool to see how a given companies public appearance might be affecting its stock. this benifits the user and the company to hold better relations through public downview.

## security:
this app is secure because there is no private information being passed in at any point. the apis search through public data with a given stock tag therefore preventing any private information leaking in. 


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
- take input form user // stock ID

- google search API 
    - [yahoo finance URL](https://finance.yahoo.com/quote/{stock_id})
- google search comapny name
    - [google search JSON API](https://developers.google.com/custom-search/v1/overview)
- scrape page for 10 articles
    - save each chsoen URL 
- **output** : output URLS 

- give URL to text analyzer

### text analyzer:
- takes in article URL
- insert into [alien text analysis API]()
    - receive positive-neutral-negitive grade
- **output** :
    - positive-neutral-negitive

- display each company result


