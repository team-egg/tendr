from aylienapiclient import textapi
from dotenv import load_dotenv
import os

load_dotenv()
APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

client = textapi.Client(APP_ID, APP_KEY)

def sentiment_analysis(url):
  """takes in one url as an argument, returns the polarity rating [positive-neutral-negative] and confidence level. """
  result = dict()
  try:
    sentiment = client.Sentiment({'url': url})
    result['polarity'] = sentiment['polarity']
    result['confidence'] = sentiment['polarity_confidence']
  except:
    result['polarity'] = 'Error'
    result['confidence'] = 'Error'
  return result
