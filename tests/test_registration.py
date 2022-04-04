"""Python Module that contains TestRegistration class"""
import pytest

from happy_bank_core.logic.registration import Registration
from happy_bank_core.logic.account import Account


class TestRegistration:
    """Class that contains Registration unittests"""

    def setup_method(self):
        """Setup method that creates test data before each test case"""
        self.test_data = {"fullname": "John Doe"}

    def test_if_register_method_returns_account_object_with_correct_data(self):
        """Tests if register method returns account with correct data"""
        # Given
        expected_name = self.test_data["fullname"]

        # When
        result = Registration.register(self.test_data)

        # Then
        assert isinstance(result, Account)
        assert result.name == expected_name
        assert result.deposit == 0

    def test_if_register_method_raises_value_error_with_empty_str(self):
        """Tests if register method raises ValueError"""
        # Given
        self.test_data["fullname"] = ""

        # When
        # Then
        with pytest.raises(ValueError):
            Registration.register(self.test_data)

    def test_if_register_method_raises_value_error_with_int(self):
        """Tests if register method raises ValueError"""
        # Given
        self.test_data["fullname"] = 1

        # When
        # Then
        with pytest.raises(ValueError):
            Registration.register(self.test_data)

    def test_if_register_method_raises_key_error(self):
        """Tests if register method raises KeyError"""
        # Given
        self.test_data = {}

        # When
        # Then
        with pytest.raises(KeyError):
            Registration.register(self.test_data)
