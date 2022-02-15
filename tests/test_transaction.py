import unittest
from happy_bank_core.logic.transaction import Transaction, TransactionException
from happy_bank_core.logic.account import Account

customer_1 = Account("id123", "John Doe", 100)
customer_2 = Account("id321", "Johanna Doe", 300)


class TestTransaction(unittest.TestCase):
    def test_insufficient_balance(self):
        """Tests if function returns false in case of insufficient balance"""

        # Given
        expected = False

        # When
        amount = 200
        result = Transaction.check_balance(customer_1, amount)

        # Then
        assert result == expected

    def test_sufficient_balance(self):
        """Tests if function returns true in case of sufficient balance"""

        # Given
        expected = True

        # When
        amount = 100
        result = Transaction.check_balance(customer_1, amount)

        # Then
        assert result == expected

    def test_zero_withdraw_amount(self):
        """Tests if function returns false if withdraw amount <= 0"""

        # Given
        expected = False

        # When
        amount = 0
        result = Transaction.check_balance(customer_1, amount)

        # Then
        assert result == expected

    def test_transfer_throws_exception_if_false(self):
        """Tests if transfer function throws exception when check_balance func returns false"""

        # When
        transfer_amount = 0

        # then
        self.assertRaises(
            TransactionException, Transaction.transfer, customer_1, customer_2, transfer_amount
        )

    def test_transfer_exception_same_id(self):
        """Tests if transfer function throws exception when sender and recipient ids are the same"""

        self.assertRaises(TransactionException, Transaction.transfer, customer_1, customer_1, 100)

    def test_transfer_returns_tuple(self):
        """Tests if transfer function returns a tuple"""

        # Given
        expected_tuple = customer_1, customer_2

        # When
        result = Transaction.transfer(customer_1, customer_2, 100)

        # Then
        self.assertTupleEqual(expected_tuple, result)


if __name__ == "__main__":
    unittest.main()
