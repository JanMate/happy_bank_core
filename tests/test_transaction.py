from happy_bank_core.logic.transaction import Transaction, TransactionException
from happy_bank_core.logic.account import Account
import pytest


class TestTransaction:
    def setup_method(self):
        self.customer_john = Account("id123", "John Doe", 100)
        self.customer_johanna = Account("id321", "Johanna Doe", 300)

    def test_insufficient_balance(self):
        """Tests if function returns false in case of insufficient balance"""

        # Given
        expected = False

        # When
        amount = 200
        result = Transaction.check_balance(self.customer_john, amount)

        # Then
        assert result == expected

    def test_sufficient_balance(self):
        """Tests if function returns true in case of sufficient balance"""

        # Given
        expected = True

        # When
        amount = 100
        result = Transaction.check_balance(self.customer_john, amount)

        # Then
        assert result == expected

    def test_zero_transferred_amount(self):
        """Tests if function returns false if withdraw amount <= 0"""

        # Given
        expected = False

        # When
        amount = 0
        result = Transaction.check_balance(self.customer_john, amount)

        # Then
        assert result == expected

    def test_transfer_throws_exception_if_false(self):
        """Tests if transfer function throws exception when check_balance func returns false"""

        # When
        transfer_amount = 0

        # then
        with pytest.raises(TransactionException):
            Transaction.transfer(self.customer_john, self.customer_johanna, transfer_amount)

    def test_thrown_exception_if_sender_and_receiver_are_same(self):
        """Tests if transfer function throws exception when sender and recipient ids are the same"""

        # When
        transfer_amount = 10

        # Then
        with pytest.raises(TransactionException):
            Transaction.transfer(self.customer_john, self.customer_john, transfer_amount)

    def test_transfer_returns_tuple_if_sender_has_enough_money_and_differs_to_receiver(self):
        """Tests if transfer function returns a tuple"""

        # Given
        expected_tuple = self.customer_john, self.customer_johanna

        # When
        result = Transaction.transfer(self.customer_john, self.customer_johanna, 100)

        # Then
        assert expected_tuple == result
