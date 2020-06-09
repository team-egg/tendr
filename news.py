from googlesearch import search 

#search key id
#get company name


#search company name
# company = 'Microsoft'

query = "Geeksforgeeks"

for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j)


# googlenews.search("Microsoft")
# result = googlenews.result()
# print(len(result))
# print('print')

# for article in range(len(result)): #default 10 articles
#     print(article)
#     for index in result[article]: #1-10
#         print(index, '\n', result[article][index])

# def search_company(company):
#     """takes in a company name string and searches google"""



# if __name__ == "__main__":
#     search_company('Microsoft')

