"""Python module that contains Registration class"""
import random
import logging

from happy_bank_core.logic.account import Account

logger = logging.getLogger(__name__)


class Registration:
    """Registration class that contains register method"""

    @staticmethod
    def register(data: dict) -> Account:
        """register method that gets dict and returns Account obj"""
        try:
            if len(data["fullname"]) == 0:
                logger.error("Received empty string instead of fullname")
                raise ValueError
            else:
                account_id = random.randint(100, 1000)
                return Account(str(account_id), data["fullname"], 0)
        except TypeError as err:
            logger.error("Incorrect data type, expected: str")
            raise err
        except KeyError as err:
            logger.error("Fullname key not found")
            raise err
