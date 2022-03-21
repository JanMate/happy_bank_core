"""Python module that contains FileConnector class"""
import json
import logging
import os

from happy_bank_core.data.connector import Connector
from happy_bank_core.logic.account import Account

logger = logging.getLogger(__name__)


class FileConnector(Connector):
    """FileConnector class that inherits from parent Connector class"""

    def __init__(self):
        super().__init__()
        self.abs_path = os.path.abspath("data/customers.json")

    def read(self, account_id):
        """Returns account with specific account id"""
        try:
            with open(self.abs_path, encoding="utf-8") as customers:
                data = json.load(customers)
                logger.info(data[account_id])
                return Account(
                    data[account_id]["id"], data[account_id]["name"], data[account_id]["deposit"]
                )
        except (FileNotFoundError, KeyError, PermissionError) as err:
            logger.error(err)
            return None

    def update(self, account):
        """Updates an existing account"""
        with open(self.abs_path, "r+", encoding="utf-8") as customers:
            data = json.load(customers)
            data[account.id] = account.__dict__
            logger.info(data)
        with open(self.abs_path, "w", encoding="utf-8") as customers:
            json.dump(data, customers, indent=2)
            return data
