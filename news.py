from googlesearch import search 

#search key id
#get company name


#search company name
company = 'Microsoft'

def search_company(company):
    """takes in a company name string and searches google"""

    for j in search(company, tld="co.in", num=10, stop=10, pause=2): 
        print(j)


if __name__ == "__main__":
    search_company('Microsoft')

