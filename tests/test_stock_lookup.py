from modules.stock_lookup import stock_to_name
from unittest.mock import patch

def test_stock_lookup_happy_path():
  actual = stock_to_name('tsla')
  expected = 'Tesla, Inc.'
  assert actual == expected

def test_stock_lookup_unhappy_path():
  with patch('builtins.input', side_effect = ['tsla']):
    actual = stock_to_name('badstock')
    expected = 'Tesla, Inc.'
    assert actual == expected