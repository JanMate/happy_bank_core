"""Python module that contains parent class Connector"""


class Connector:
    """Parent class for memory, file and redis connectors"""

    def __init__(self):
        """Calls the Connector class constructor"""

    def read(self, account_id):
        """Returns account with specific account id"""

    def update(self, account):
        """Updates an existing account"""
