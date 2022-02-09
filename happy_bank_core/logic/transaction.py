class Transaction:

    def __init__(self, customer_id, balance):
        self.balance = balance
        self.customer_id = customer_id

    def __eq__(self, other):
        return self.customer_id == other.customer_id

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Following amount {amount} has been withdrawn from bank account ID: {self.customer_id}')
            print(f'Current balance: {self.balance}')
            return self.balance
        else:
            print("insufficient funds or incorrect amount, withdraw amount should be > 0")
            exit()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Following amount {amount} has been added to bank account ID: {self.customer_id}')
            print(f'Current balance: {self.balance}')
            return self.balance
        else:
            print("Amount cannot be 0 or negative number, please try again")
            exit()

    @staticmethod
    def transfer(sender_id, receiver_id, amount):
        if sender_id == receiver_id:
            print("You cannot transfer money to your own bank account, please try again with the correct recipient ID")
            exit()
        else:
            return sender_id.withdraw(amount), receiver_id.deposit(amount)
