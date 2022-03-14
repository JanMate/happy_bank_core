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

    def test_if_read_function_returns_account_instance(self):
        """Tests if read function returns account instance"""

        # When
        result = self.memory.read("id321")

        # Then
        assert isinstance(result, Account)

    def test_if_read_function_returns_account_with_correct_id(self):
        """Tests if read function returns account with correct ID"""

        # Given
        expected_id = "id321"

        # When
        result = self.memory.read(expected_id)

        # Then
        assert expected_id == result.id

    def test_if_read_function_throws_account_not_found_exception(self):
        """Tests if read function throws AccountNotFound exception"""

        # When
        account_id = "does not exist"

        # Then
        with pytest.raises(AccountNotFoundException):
            self.memory.read(account_id)

    def test_read_func_returns_updated_account(self):
        """Tests if update function returns updated data"""

        # Given
        updated_account = Account("id321", "John Doe", 50)

        # When
        result = self.memory.update(updated_account)

        # Then
        assert self.accounts != result
