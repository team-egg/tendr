from modules.sentiment_analysis import sentiment_analysis

def test_sentiment_analysis_positive():
  result = sentiment_analysis('https://www.axios.com/tesla-stock-most-valuable-car-company-2765c5d0-b31f-400c-a921-0f8545480ddc.html')
  actual = result['polarity']
  expected = 'positive'
  assert actual == expected

def test_sentiment_analysis_negative():
  result = sentiment_analysis('https://www.cnn.com/2020/06/09/tech/elon-musk-tesla-restart-factory-problems-covid-19/index.html')
  actual = result['polarity']
  expected = 'negative'
  assert actual == expected

def test_sentiment_analysis_neutral():
  result = sentiment_analysis('https://thedriven.io/2020/06/11/tesla-battery-offshoot-backed-by-st-baker-fund-flags-major-cost-breakthrough/')
  actual = result['polarity']
  expected = 'neutral'
  assert actual == expected
