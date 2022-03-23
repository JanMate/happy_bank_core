"""Python Module that contains TestFileConnector class"""
from unittest.mock import patch, mock_open

import pytest

from happy_bank_core.data.file_connector import FileConnector
from happy_bank_core.logic.account import Account


READ_TEST_DATA = (
    '{"101": {"id": "101", "name": "John Doe", "deposit": 1000}, '
    '"102": {"id": "102", "name": "Johanna Doe", "deposit": 1000}}'
)


class TestFileConnector:
    """Class that contains FileConnector unittests"""

    def setup_method(self):
        """Setup method that creates FileConnector class instance before each test case"""
        self.file_connector = FileConnector()

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_read_func_returns_account_with_correct_id(self, mocked_open):
        """Tests if read function returns account with correct ID"""

        # Given
        expected_id = "102"

        # When
        result = self.file_connector.read(expected_id)

        # Then
        mocked_open.assert_called_once()
        assert isinstance(result, Account)
        assert expected_id == result.id

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_read_function_raises_key_error(self, mocked_open):
        """Tests if read function raises KeyError exception"""

        # When
        mocked_open.side_effect = KeyError()

        # Then
        with pytest.raises(KeyError):
            self.file_connector.read("101")
        mocked_open.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_read_func_raises_file_not_found_error(self, mocked_open):
        """Tests if read function raises FileNotFound exception"""

        # When
        mocked_open.side_effect = FileNotFoundError()

        # Then
        with pytest.raises(FileNotFoundError):
            self.file_connector.read("103")
        mocked_open.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_read_func_raises_permission_error(self, mocked_open):
        """Tests if read function raises PermissionError exception"""

        # When
        mocked_open.side_effect = PermissionError()

        # Then
        with pytest.raises(PermissionError):
            self.file_connector.read("103")
        mocked_open.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_returns_updated_values(self, mocked_open):
        """Tests if update function returns updated data"""

        # Given
        account = Account("101", "John Doe", 2000)

        # When
        result = self.file_connector.update(account)

        # Then
        assert result != READ_TEST_DATA
        mocked_open.assert_called()

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_raises_permission_error(self, mocked_open):
        """Tests if update function raises PermissionError exception"""
        # Given
        account = Account("101", "John Doe", 2000)

        # When
        mocked_open.side_effect = PermissionError()

        # Then
        with pytest.raises(PermissionError):
            self.file_connector.update(account)
        mocked_open.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_raises_key_error(self, mocked_open):
        """Tests if update function raises KeyError exception"""
        # Given
        account = Account("101", "John Doe", 2000)

        # When
        mocked_open.side_effect = KeyError()

        # Then
        with pytest.raises(KeyError):
            self.file_connector.update(account)
        mocked_open.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_raises_file_not_found_error(self, mocked_open):
        """Tests if update function raises FileNotFound exception"""
        # Given
        account = Account("101", "John Doe", 2000)

        # When
        mocked_open.side_effect = FileNotFoundError()

        # Then
        with pytest.raises(FileNotFoundError):
            self.file_connector.update(account)
        mocked_open.assert_called_once()
