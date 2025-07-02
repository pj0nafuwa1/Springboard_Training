import uuid  # To generate a unique account ID

class Account:
    def __init__(self, customer_id, account_type, balance=0.0):
        # Each account has a unique ID and is linked to a customer
        self.account_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.account_type = account_type  # checking or savings
        self.balance = balance

    def deposit(self, amount):
        # Adds money to the balance
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        # Subtracts money if there is enough balance
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def to_dict(self):
        # Converts account object to dictionary for JSON storage
        return {
            "account_id": self.account_id,
            "customer_id": self.customer_id,
            "account_type": self.account_type,
            "balance": self.balance
        }

