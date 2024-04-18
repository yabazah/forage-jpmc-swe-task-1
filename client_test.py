import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), round((float(quote['top_bid']['price'])+float(quote['top_ask']['price']))/2, 2)))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), round((float(quote['top_bid']['price'])+float(quote['top_ask']['price']))/2, 2)))


  """ ------------ Add more unit tests ------------ """
  # add test for getRatio
  def test_getRatio_SameNum(self):
    # price for one stock
    price_a = 100
    # price of other stock
    price_b = 100
    self.assertEqual(getRatio(price_a, price_b), price_a/price_b)

  def test_getRatio_ABiggerThanB(self):
    price_a = 150
    price_b = 100
    self.assertEqual(getRatio(price_a, price_b), price_a/price_b)

  def test_getRatio_ASmallerThanB(self):
    price_a = 100
    price_b = 150
    self.assertEqual(getRatio(price_a, price_b), price_a/price_b)

  def test_getRatio_AEqualsZero(self):
    price_a = 0
    price_b = 100
    self.assertEqual(getRatio(price_a,price_b), price_a/price_b)

  def test_getRatio_BEqualsZero(self):
    price_a = 100
    price_b = 0
    self.assertEqual(getRatio(price_a, price_b), None)



if __name__ == '__main__':
    unittest.main()
