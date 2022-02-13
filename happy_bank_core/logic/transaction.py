from account import Account
from account import accounts

a1 = Account("#1234")
a2 = Account("#12345")


class Transaction:
    @staticmethod
    def check_balance(customer, amount):
        """Verifies if customer has enough money to transfer"""
        amount = float(amount)
        balance = customer.deposit
        if 0 < amount <= balance:
            return True
        else:
            return False

    @staticmethod
    def transfer(sender, recipient, amount):
        """Ensures transfer between 2 accounts"""
        if sender.id == recipient.id:
            print(
                "Accounts are equal, please enter correct account ID\n"
                "----------------------------------------------------"
            )
        elif not Transaction.check_balance(sender, amount):
            print(
                "insufficient funds or incorrect amount was entered, "
                "please try again\n"
                "----------------------------------------------------"
            )
        else:
            sender.deposit = round((sender.deposit - amount), 2)
            recipient.deposit = round((recipient.deposit + amount), 2)

            accounts[sender.id]["deposit"] = sender.deposit
            accounts[recipient.id]["deposit"] = recipient.deposit

            print(
                f"Following amount {amount} has been transferred "
                f"from account {sender.id} to account {recipient.id}\n"
                f"Current {sender.id} balance: {sender.deposit};\n"
                f"Current {recipient.id} balance: {recipient.deposit}\n"
                f"---------------------------------------------------"
            )
