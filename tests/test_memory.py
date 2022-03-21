"""Python module that contains MemoryConnector unittests"""
from happy_bank_core.data.memory import MemoryConnector
from happy_bank_core.logic.account import Account


class TestMemoryConnector:
    """Class that contains MemoryConnector unittests"""

    def setup_method(self):
        """Setup method that creates list of account and MemoryConnector class instance"""
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
        expected_id = list(self.accounts.keys())[0]

        # When
        result = self.memory.read(expected_id)

        # Then
        assert expected_id == result.id

    def test_if_read_function_throws_account_not_found_exception(self):
        """Tests if read function throws KeyError exception"""

        # When
        result = self.memory.read("does_not_exist")

        # Then
        assert not result

    def test_read_func_returns_updated_account(self):
        """Tests if update function returns updated data"""

        # Given
        expected_deposit = 2000
        updated_account = list(self.accounts.items())[0][1]
        updated_account.deposit = expected_deposit

        # When
        self.memory.update(updated_account)

        # Then
        assert expected_deposit == self.memory.accounts["id321"].deposit
