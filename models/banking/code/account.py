import uuid  # To generate a unique account ID

class Account:
    """Represents a bank account linked to a customer."""
    def __init__(self, customer_id, account_type, balance=0.0):
        """
        Initialize an Account object.
        Args:
            customer_id (str): The ID of the customer who owns the account.
            account_type (str): The type of account (checking or savings).
            balance (float): Initial balance (default 0.0).
        """
        self.account_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.account_type = account_type  # checking or savings
        self.balance = balance

    def deposit(self, amount):
        """Add money to the balance."""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Subtract money if there is enough balance."""
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def to_dict(self):
        """Convert account object to dictionary for JSON storage."""
        return {
            "account_id": self.account_id,
            "customer_id": self.customer_id,
            "account_type": self.account_type,
            "balance": self.balance
        }

