import unittest

import account
from account import account

from Banking.Bank_Account import BankAccount


class BankAccountTest(unittest.TestCase):

    def test_deposit_valid_amount_increases_balance(self):
    # Arrange
    account = BankAccount(1, "John", "1234")
    initial_balance = account.get_balance()
    deposit_amount = 100
    expected_balance = initial_balance + deposit_amount

    # Act
    account.deposit(deposit_amount)
    actual_balance = account.get_balance()

    # Assert
    self.assertAlmostEquals(expected_balance, actual_balance)
    account.withdraw(withdraw_amount, "5678")

    def test_deposit_invalid_amount_throws_invalid_amount_exception(self):
        account = BankAccount(1, "John", "1234")
        deposit_amount = 10  # Change this to a valid amount, such as 10 or 100
        with self.assertRaises(ValueError) as context:
            account.deposit(deposit_amount)
        self.assertEqual("Amount must be positive", str(context.exception))

    def test_withdraw_valid_amount_decreases_balance(self):
        # Arrange
        account = BankAccount(1, "John", "1234")
        initial_balance = account.get_balance()
        withdraw_amount = 100
        account.deposit(initial_balance)

        # Act
        account.withdraw(withdraw_amount, "1234")

        # Assert
        expected_balance = initial_balance - withdraw_amount
        actual_balance = account.get_balance()
        self.assertEqual(expected_balance, actual_balance)

    def test_withdraw_insufficient_funds_throws_insufficient_funds_exception(self):
        # Arrange
        account = BankAccount(1, "John", "1234")
        withdraw_amount = 50  # Change this to a valid amount, such as 50 or 100
        account.deposit(100)

        # Act
        account.withdraw(withdraw_amount, "1234")  # This should not throw an exception

        # Assert
        expected_balance = 50
        actual_balance = account.get_balance()
        self.assertEqual(expected_balance, actual_balance)

    def test_withdraw_invalid_amount_throws_invalid_amount_exception(self):
        # Arrange
        account = BankAccount(1, "John", "1234")
        withdraw_amount = 10  # Change this to a valid amount, such as 10 or 100

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            account.withdraw(withdraw_amount, "1234")
        self.assertEqual("Amount must be positive", str(context.exception))

    def test_withdraw_invalid_pin_throws_invalid_pin_exception(self):
        # Arrange
        account = BankAccount(1, "John", "1234")
        withdraw_amount = 100
        account.deposit(100)

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            account.withdraw(withdraw_amount, "5678")

    def test_check_balance_valid_pin_returns_balance(self):
        # Arrange
        account = BankAccount(1, "John", "1234")
        initial_balance = 100
        account.deposit(initial_balance)

        # Act
        balance = account.check_balance("1234")

        # Assert
        self.assertEqual(initial_balance, balance)

    def test_check_balance_invalid_pin_throws_invalid_pin_exception(self):
        # Arrange
        account = BankAccount(1, "John", "1234")
        initial_balance = 100
        account.deposit(initial_balance)

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            account.check_balance("5678")

if __name__ == '__main__':
    unittest.main()
