from modules.news_search import google_news
from modules.stock_lookup import stock_to_name
from aylienapiclient import textapi
from alive_progress import alive_bar 
from textwrap import dedent
from modules.sentiment_ananlysis import sentiment_analysis

import time

class Tendr:
    def __init__(self):
        self.id = None
        self.name = None

    def get_url(self):
        """returns company article URL"""
        stock_id = self.id
        company = stock_to_name(stock_id)
        self.name = company
        return google_news(company)

    def get_sentiment_report(self):
        """returns report of positive/negative article counts, and total score"""
        urls = self.get_url()
        results = list()
        pos_count = 0
        neg_count = 0
        neu_count = 0

        score = 0
        # neg_score = 0

        # client = textapi.Client("YOUR_APP_ID", "YOUR_APP_KEY")
        with alive_bar(len(urls)) as bar:
            for url in urls:
                result = sentiment_analysis(url)
                # print(result)
                if result['polarity'] == 'negative':
                    neg_count += 1
                    # neg_score += result['confidence']
                elif result['polarity'] == 'positive':
                    pos_count += 1
                    score += 0.5
                else:
                    neu_count += 1
                    score += 0.25

                bar()
                time.sleep(0.5)

        report = dedent(f"""For the company {self.name}, among {len(urls)} news articles, there're:
        {pos_count} articles showing positive sentiment
        {neg_count} articles showing negative sentiment 
        {neu_count} articles showing neutral sentiment
        The overall socre (1-10 scale) is : {score}
        """)
        return report
                
    def start(self):
        """initializes Tendr methods and prints report to console"""
        stock_id = input("Enter in the company's stock ID you'd like to get info: ")
        self.id = stock_id
        print(self.get_sentiment_report())
        


if __name__ == "__main__":
    
    test = Tendr()
    test.start()
