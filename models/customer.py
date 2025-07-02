import uuid # Generating unique customer IDs

class Customer:
    def __init__(self, first_name, last_name, address):
        # Assign a unique ID to each customer
        self.customer_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def get_full_name(self):
        # Returns the full name of the customer
        return f"{self.first_name} {self.last_name}"

    def update_address(self, new_address):
        # Updates the customer's address
        self.address = new_address

    def to_dict(self):
        # Converts the customer object to a dictionary, the plan is to store in JSON format
        return {
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address
        }
