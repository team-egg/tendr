from modules.news_search import google_news

def test_google_news():
  actual = len(google_news('Apple'))
  expected = 20
  assert actual == expected
