from happy_bank_core.data.connector import Connector
from happy_bank_core.logic.account import Account
import json
import logging
import os

logger = logging.getLogger(__name__)

abs_path = os.path.abspath("data/customers.json")


class FileConnector(Connector):
    def __init__(self):
        pass

    @staticmethod
    def read(account_id):
        try:
            with open(abs_path) as customers:
                data = json.load(customers)
                logger.info(data[account_id])
                return Account(
                    data[account_id]["id"], data[account_id]["name"], data[account_id]["deposit"]
                )
        except FileNotFoundError as e:
            logger.error(e)
            return None

    @staticmethod
    def update(account):
        with open(abs_path, "r+") as customers:
            data = json.load(customers)
            data[account.id] = account.__dict__
            logger.info(data)
        with open(abs_path, "w") as customers:
            json.dump(data, customers, indent=2)
            return data
