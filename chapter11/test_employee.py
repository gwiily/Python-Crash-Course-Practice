import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.liming = Employee('li', 'ming', 8000)

	def test_give_default_raise(self):
		self.liming.give_raise()
		self.assertEqual(13000, self.liming.salary)

	def test_give_custom_raise(self):
		self.liming.give_raise(2000)
		self.assertEqual(10000, self.liming.salary)

unittest.main()