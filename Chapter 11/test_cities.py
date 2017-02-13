import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
	"""Test for city_functions.py"""
	
	def test_city_country(self):
		testcase = city_country('santiago', 'chile')
		self.assertEqual(testcase, 'Santiago, Chile')
	
	def test_city_country_population(self):
		testcase = city_country('santiago', 'chile', '5000000')
		self.assertEqual(testcase, 'Santiago, Chile - population 5000000')
	
unittest.main()
