import uuid  # Generating unique customer IDs


class Customer:
    """Represents a bank customer."""

    def __init__(self, first_name, last_name, address):
        """
        Initialize a Customer object.

        Args:
            first_name (str): Customer's first name.
            last_name (str): Customer's last name.
            address (str): Customer's address.
        """
        # Assign a unique ID to each customer
        self.customer_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def get_full_name(self):
        """Return the full name of the customer."""
        return f"{self.first_name} {self.last_name}"

    def update_address(self, new_address):
        """Update the customer's address."""
        self.address = new_address

    def to_dict(self):
        """Convert the customer object to a dictionary for JSON storage."""
        return {
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
        }
