import json

from happy_bank_core.data.file_connector import FileConnector
from happy_bank_core.logic.account import Account
import pytest
from unittest import mock


class TestFileConnector:
    def setup_method(self):
        self.read_data = (
            '{"101": {"id": "101", "name": "John Doe", "deposit": 1000},'
            ' "102": {"id": "102", "name": "Johanna Doe", "deposit": 1000}}'
        )
        self.mock_data = mock.mock_open(read_data=self.read_data)

    def test_if_read_function_returns_account_object(self):
        with mock.patch("builtins.open", self.mock_data):
            result = FileConnector.read("102")
            assert isinstance(result, Account)

    def test_if_read_function_throws_key_error(self):
        with mock.patch("builtins.open", self.mock_data):
            with pytest.raises(KeyError):
                FileConnector.read("103")

    def test_if_read_func_throws_file_not_found_error(self):
        with mock.patch("builtins.open") as mocked_open:
            mocked_open.side_effect = FileNotFoundError()
            result = FileConnector.read("103")
            assert not result

    def test_if_update_func_returns_updated_values(self):
        with mock.patch("builtins.open", self.mock_data):
            account = Account("101", "John Doe", 2000)
            result = FileConnector.update(account)
            assert result != self.read_data
