from happy_bank_core.data.connector import Connector
from happy_bank_core.logic.account import Account
import logging

logger = logging.getLogger(__name__)


class AccountNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class MemoryConnector(Connector):
    def __init__(self):
        self.accounts = {
            "id321": Account("id321", "Johan Doe", 1000),
            "id123": Account("id123", "John Doe", 1000),
            "id456": Account("id456", "Johanna Doe", 1000),
        }

    def read(self, account_id):
        try:
            logger.info(self.accounts[account_id])
            return self.accounts[account_id]
        except KeyError:
            raise AccountNotFoundException("Account not found")

    def update(self, account):
        self.accounts[account.id] = account
        logger.info(self.accounts)
        return self.accounts
