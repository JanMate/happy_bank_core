"""Python Module that contains TestFileConnector class"""
from unittest import mock
import json
import pytest

from happy_bank_core.data.file_connector import FileConnector
from happy_bank_core.logic.account import Account
from tests import abs_paths

READ_TEST_DATA = (
    '{"101": {"id": "101", "name": "John Doe", "deposit": 1000}, '
    '"102": {"id": "102", "name": "Johanna Doe", "deposit": 1000}}'
)


# pylint: disable=attribute-defined-outside-init
class TestFileConnector:
    """Class that contains FileConnector unittests"""

    def setup_method(self):
        """Setup method that creates FileConnector and Account instances before each test case"""
        self.accounts = json.loads(READ_TEST_DATA)
        self.account_id = "101"
        self.account = Account(
            self.accounts[self.account_id]["id"],
            self.accounts[self.account_id]["name"],
            self.accounts[self.account_id]["deposit"],
        )
        self.file_connector = FileConnector()

    @mock.patch(abs_paths.READ_FUNC_ABS_PATH, new_callable=mock.mock_open, read_data=READ_TEST_DATA)
    def test_if_read_func_returns_account_with_correct_id(self, mocked_open):
        """Tests if read function returns account with correct ID"""
        # Given
        expected_id = self.account_id
        expected_account = self.account

        # When
        result = self.file_connector.read(expected_id)

        # Then
        assert isinstance(result, Account)
        assert expected_id == result.id
        assert expected_account.name == result.name
        assert expected_account.deposit == result.deposit
        mocked_open.assert_called_once()

    @mock.patch(abs_paths.READ_FUNC_ABS_PATH, new_callable=mock.mock_open, read_data=READ_TEST_DATA)
    def test_if_read_function_raises_key_error(self, mocked_open):
        """Tests if read function raises KeyError exception"""
        # Given
        mocked_open.side_effect = KeyError()

        # When
        # Then
        with pytest.raises(KeyError):
            self.file_connector.read("101")
        mocked_open.assert_called_once()

    @mock.patch(abs_paths.READ_FUNC_ABS_PATH, new_callable=mock.mock_open, read_data=READ_TEST_DATA)
    def test_if_read_func_raises_file_not_found_error(self, mocked_open):
        """Tests if read function raises FileNotFound exception"""
        # Given
        mocked_open.side_effect = FileNotFoundError()

        # When
        # Then
        with pytest.raises(FileNotFoundError):
            self.file_connector.read("103")
        assert mocked_open.call_count == 2

    @mock.patch(abs_paths.READ_FUNC_ABS_PATH, new_callable=mock.mock_open, read_data=READ_TEST_DATA)
    def test_if_read_func_raises_permission_error(self, mocked_open):
        """Tests if read function raises PermissionError exception"""
        # Given
        mocked_open.side_effect = PermissionError()

        # When
        # Then
        with pytest.raises(PermissionError):
            self.file_connector.read("103")
        mocked_open.assert_called_once()

    @mock.patch(abs_paths.get_abs_path_of_type(json.dump), return_value=None)
    @mock.patch(abs_paths.get_abs_path_of_type(json.load), return_value=json.loads(READ_TEST_DATA))
    @mock.patch(abs_paths.READ_FUNC_ABS_PATH, new_callable=mock.mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_returns_updated_values(self, mocked_open, mocked_load, mocked_dump):
        """Tests if update function returns updated data"""
        # Given
        self.account.deposit = 2000
        load_return_value = mocked_load.return_value
        load_return_value[self.account.id]["deposit"] = self.account.deposit

        # When
        self.file_connector.update(self.account)

        # Then
        mocked_open.assert_called_with(self.file_connector.abs_path, "w", encoding="utf-8")
        mocked_load.assert_called_once_with(mocked_open.return_value)
        mocked_dump.assert_called_once_with(load_return_value, mocked_open.return_value, indent=2)

    @mock.patch(abs_paths.READ_FUNC_ABS_PATH, new_callable=mock.mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_raises_permission_error(self, mocked_open):
        """Tests if update function raises PermissionError exception"""
        # Given
        mocked_open.side_effect = PermissionError()

        # When
        # Then
        with pytest.raises(PermissionError):
            self.file_connector.update(self.account)
        mocked_open.assert_called_once()

    @mock.patch(abs_paths.READ_FUNC_ABS_PATH, new_callable=mock.mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_raises_key_error(self, mocked_open):
        """Tests if update function raises KeyError exception"""
        # Given
        mocked_open.side_effect = KeyError()

        # When
        # Then
        with pytest.raises(KeyError):
            self.file_connector.update(self.account)
        mocked_open.assert_called_once()

    @mock.patch(abs_paths.READ_FUNC_ABS_PATH, new_callable=mock.mock_open, read_data=READ_TEST_DATA)
    def test_if_update_func_raises_file_not_found_error(self, mocked_open):
        """Tests if update function raises FileNotFound exception"""
        # Given
        mocked_open.side_effect = FileNotFoundError()

        # When
        # Then
        with pytest.raises(FileNotFoundError):
            self.file_connector.update(self.account)
        assert mocked_open.call_count == 2
