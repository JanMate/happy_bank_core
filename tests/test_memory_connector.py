"""Python module that contains MemoryConnector unittests"""
import pytest

from happy_bank_core.data.memory_connector import MemoryConnector
from happy_bank_core.logic.account import Account


# pylint: disable=attribute-defined-outside-init
class TestMemoryConnector:
    """Class that contains MemoryConnector unittests"""

    def setup_method(self):
        """Setup class method that creates list of account and MemoryConnector class instance"""
        self.accounts = {
            "id321": Account("id321", "Johan Doe", 1000),
            "id123": Account("id123", "John Doe", 1000),
            "id456": Account("id456", "Johanna Doe", 1000),
        }
        self.memory = MemoryConnector()

    def test_if_read_function_returns_account_with_correct_id(self):
        """Tests if read function returns account with correct ID"""
        # Given
        expected_id = list(self.accounts.keys())[0]

        # When
        result = self.memory.read(expected_id)

        # Then
        assert isinstance(result, Account)
        assert result.id == expected_id
        assert result.name == self.accounts[expected_id].name
        assert result.deposit == self.accounts[expected_id].deposit

    def test_if_read_function_throws_account_not_found_exception(self):
        """Tests if read function throws KeyError exception"""
        # When
        # Then
        with pytest.raises(KeyError):
            self.memory.read("does_not_exist")

    def test_if_update_updates_deposit_in_given_account_returns_void(self):
        """Tests if update function returns updated data"""
        # Given
        expected_deposit = 2000
        updated_account = list(self.accounts.values())[0]
        account_id = updated_account.id
        updated_account.deposit = expected_deposit

        # When
        self.memory.update(updated_account)

        # Then
        assert updated_account.deposit == self.memory.accounts[account_id].deposit
        assert updated_account.id == self.memory.accounts[account_id].id
        assert updated_account.name == self.memory.accounts[account_id].name

    def test_if_update_func_raises_key_error(self):
        """Tests if update function raises KeyError"""
        # When
        # Then
        with pytest.raises(KeyError):
            self.memory.update(self.accounts["does_not_exist"])
