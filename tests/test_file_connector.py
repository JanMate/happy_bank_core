from happy_bank_core.data.file_connector import FileConnector
from happy_bank_core.logic.account import Account
import pytest
from unittest.mock import patch, mock_open

READ_TEST_DATA = (
    '{"101": {"id": "101", "name": "John Doe", "deposit": 1000}, '
    '"102": {"id": "102", "name": "Johanna Doe", "deposit": 1000}}'
)


class TestFileConnector:
    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_read_function_returns_account_instance(self, mock_read):
        """Tests if read function returns account instance"""

        # When
        result = FileConnector.read("102")

        # Then
        mock_read.assert_called_once()
        assert isinstance(result, Account)

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_read_func_return_account_with_correct_id(self, mock_read):
        """Tests if read function returns account with correct ID"""

        # Given
        expected_id = "102"

        # When
        result = FileConnector.read(expected_id)

        # Then
        mock_read.assert_called_once()
        assert expected_id == result.id

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_read_function_throws_key_error(self, mock_read):
        """Tests if read function throws KeyError exception"""

        # Then
        with pytest.raises(KeyError):
            FileConnector.read("103")
        mock_read.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_read_func_throws_file_not_found_error(self, mock_read):
        """Tests if read function throws FileNotFound exception"""

        # When
        mock_read.side_effect = FileNotFoundError()
        result = FileConnector.read("103")

        # Then
        mock_read.assert_called_once()
        assert not result

    @patch("builtins.open", new_callable=mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_returns_updated_values(self, mock_read):
        """Tests if update function returns updated data"""

        # Given
        account = Account("101", "John Doe", 2000)

        # When
        result = FileConnector.update(account)

        # Then
        assert result != READ_TEST_DATA
        mock_read.assert_called()
