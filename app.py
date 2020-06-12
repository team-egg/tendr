from modules.news_search import google_news
from modules.stock_lookup import stock_to_name
from aylienapiclient import textapi
from alive_progress import alive_bar 
from textwrap import dedent
from modules.sentiment_analysis import sentiment_analysis
import time

class Tendr:
    def __init__(self):
        self.id = None
        self.name = None
        self.pos_count = 0
        self.neg_count = 0
        self.neu_count = 0
        self.error_count = 0

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

        score = 0

        with alive_bar(len(urls)) as bar:
            for url in urls:
                result = sentiment_analysis(url)
                if result['polarity'] == 'negative':
                    self.neg_count += 1
                elif result['polarity'] == 'positive':
                    self.pos_count += 1
                    score += 0.5
                elif result ['polarity'] == 'Error':
                    self.error_count += 1
                    score += 0.25
                else:
                    self.neu_count += 1
                    score += 0.25

                bar()
                time.sleep(0.5)

        report = f"""
        For the company {self.name}, among {len(urls)} news articles, there are:
        {self.pos_count} articles showing positive sentiment
        {self.neg_count} articles showing negative sentiment 
        {self.neu_count} articles showing neutral sentiment
        {self.error_count} articles can't be analyzed due to error
        The overall score (1-10 scale) is : {score}
        """
        return report
                
    def start(self):
        """initializes Tendr methods and prints report to console"""
        stock_id = input("Enter in the company's stock ID you'd like to get info: ")
        self.id = stock_id
        print(dedent(self.get_sentiment_report()))
        
    def visual_report(self,stock_id):
        """used by jupyter lab"""
        self.id = stock_id
        self.get_sentiment_report()
    



if __name__ == "__main__":
    
    test = Tendr()
    test.get_url()
