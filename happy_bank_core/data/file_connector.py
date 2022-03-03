from happy_bank_core.data.connector import Connector
import json
import logging

logger = logging.getLogger(__name__)


class FileConnector(Connector):
    def __init__(self):
        pass

    def read(self, account_id):
        try:
            with open("customers.json") as customers:
                data = json.load(customers)
                logger.info(data[account_id])
                return data[account_id]
        except FileNotFoundError as e:
            logger.error(e)
            return e

    def update(self, account):
        with open("customers.json", "r+") as customers:
            data = json.load(customers)
            data[account.id] = account.__dict__
            logger.info(data)
        with open("customers.json", "w") as customers:
            json.dump(data, customers, indent=2)
