import uuid  # For unique employee IDs


class Employee:
    """Represents a bank employee."""

    def __init__(self, name, position):
        """
        Initialize employee with unique ID, name, and position.
        Args:
            name (str): Employee's name.
            position (str): Employee's job position.
        """
        self.employee_id = str(uuid.uuid4())
        self.name = name
        self.position = position

    def to_dict(self):
        """Serialize employee object to dictionary."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position,
        }
