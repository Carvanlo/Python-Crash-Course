class Employee():
	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary
		
	def give_raise(self, raise_amount=5000):
		self.annual_salary += raise_amount
		
import unittest

class TestEmployee(unittest.TestCase):
	"""Test for the class Employee."""
	
	def setUp(self):
		self.employee_case = Employee('Carmelo', 'Anthony', 50000)
				
	def test_give_default_raise(self):
		self.employee_case.give_raise()
		self.assertEqual(self.employee_case.annual_salary, 55000)
		
	def test_give_custom_raise(self):
		self.employee_case.give_raise(10000)
		self.assertEqual(self.employee_case.annual_salary, 60000) 

unittest.main()
