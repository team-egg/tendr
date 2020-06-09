from googlesearch import search 

#from eugenes_file.py.module import company_return_variable as company

#search key id
# get company name

#search company name
# company = company
company = 'Microsoft'

check_str = isinstance(company, str)
print_check = print('*** is company a string? : ' + str(check_str) + ' ***')

add_news = ' news'
query = company + add_news

view_query = f"""
{"*"*40}
*** search query : {query} ***
{"*"*40}"""

url_list =[]
def search_company(query):
    """takes in a company name string and searches google"""
    print(view_query)

    #search ( , domain=google.com or .in, num=how many, stop=last result, pause=cooldown)
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        print(j)
        url_list.append(j)
    # print(url_list)
    return url_list

#give url list to pengs file to grab text and analyze
if __name__ == "__main__":
    search_company('Microsoft news')
