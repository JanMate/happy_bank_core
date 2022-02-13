accounts = dict()
accounts["#1234"] = {"name": "John Doe", "deposit": 1000}
accounts["#12345"] = {"name": "Johanna Doe", "deposit": 2000}


class Account:
    def __init__(self, customer):
        """Gets customer's data from accounts dictionary"""
        self.id = customer
        self.name = accounts[self.id]["name"]
        self.deposit = float(accounts[self.id]["deposit"])

    def __str__(self):
        return f"Customer ID: {self.id};\n Name: {self.name};\n " f"Balance: {self.deposit}"
