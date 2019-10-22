import unittest
from account import Account

class TestBank(unittest.TestCase):

	def test_deposit(self):
		accountTest = Account(123,10000)
		self.assertEqual(accountTest.deposit(30000), 40000, "Should be 40000")

	def test_withdraw(self):
		accountTest = Account(123,10000)
		self.assertEqual(accountTest.withdraw(5000), 5000, "Should be 5000")

	def test_withdraw_negative(self):
		accountTest = Account(123,10000)
		self.assertEqual(accountTest.withdraw(50000), -40500, "Should be 40500")

	def test_double_withdraw_negative(self):
		accountTest = Account(123,10000)
		self.assertEqual(accountTest.withdraw(50000), -40500, "Should be 40500")
		self.assertEqual(accountTest.withdraw(50000), -91000, "Should be 91000")

if __name__ == '__main__':
    unittest.main()