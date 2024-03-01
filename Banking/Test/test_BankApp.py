import unittest
from unittest.mock import patch
from io import StringIO
from bank_app import Bank, BankApp

class test_BankApp(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_register_customer(self):
        self.bank.register_customer("Alice", "1234")
        self.assertEqual(len(self.bank.accounts), 1)

    def test_deposit(self):
        self.bank.register_customer("Alice", "1234")
        self.bank.deposit(1, 100)
        self.assertEqual(self.bank.accounts[0]["balance"], 100)

    def test_withdraw(self):
        self.bank.register_customer("Alice", "1234")
        self.bank.deposit(1, 100)
        self.bank.withdraw(1, 50, "1234")
        self.assertEqual(self.bank.accounts[0]["balance"], 50)

    def test_transfer(self):
        self.bank.register_customer("Alice", "1234")
        self.bank.register_customer("Bob", "5678")
        self.bank.deposit(1, 100)
        self.bank.transfer(1, 2, 50, "1234")
        self.assertEqual(self.bank.accounts[0]["balance"], 50)
        self.assertEqual(self.bank.accounts[1]["balance"], 50)

    def test_check_balance(self):
        self.bank.register_customer("Alice", "1234")
        self.bank.deposit(1, 100)
        balance = self.bank.check_balance(1, "1234")
        self.assertEqual(balance, 100)

    def test_remove_account(self):
        self.bank.register_customer("Alice", "1234")
        self.bank.remove_account(1, "1234")
        self.assertEqual(len(self.bank.accounts), 0)

if __name__ == '__main__':
    unittest.main()
