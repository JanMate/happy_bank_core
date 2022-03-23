"""Python module that contains parent class Connector"""
from abc import ABC, abstractmethod


class Connector(ABC):
    """Parent class for data source connectors"""

    @abstractmethod
    def read(self, account_id):
        """Returns account with specific account id"""

    @abstractmethod
    def update(self, account):
        """Updates an existing account"""
