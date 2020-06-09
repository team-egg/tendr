from googlesearch import search 

#from /eugenes_file/file.py import company_variable as company

#search key id
# get company name

#search company name
# company = company
company = 'Apple'

add_news = ' news'
query = company + add_news

view_query = f"""
{"*"*40}
*** search query : {query} ***
{"*"*40}"""

def search_company(query):
    """takes in a company name string and searches google"""
    print(view_query)

    #search ( , domain=google.com or .in, num=how many, stop=last result, pause=cooldown)
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        print(j)


if __name__ == "__main__":
    search_company('Microsoft news')
    search_company('Apple news')


