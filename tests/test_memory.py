from happy_bank_core.data.memory import AccountNotFoundException, MemoryConnector
from happy_bank_core.logic.account import Account
import pytest


class TestMemory:
    def setup_method(self):
        self.accounts = {
            "id321": Account("id321", "Johan Doe", 1000),
            "id123": Account("id123", "John Doe", 1000),
            "id456": Account("id456", "Johanna Doe", 1000),
        }
        self.memory = MemoryConnector()

    def test_if_read_function_returns_account_object(self):

        # When
        result = self.memory.read("id321")

        # Assert
        assert isinstance(result, Account)

    def test_thrown_exception_if_account_not_found(self):

        # Assert
        with pytest.raises(AccountNotFoundException):
            self.memory.read("non_existing_id")

    def test_read_func_returns_updated_account(self):

        # Given
        updated_account = Account("id321", "John Doe", 50)
        result = self.memory.update(updated_account)

        # Assert
        assert self.accounts != result
