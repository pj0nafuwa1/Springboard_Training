import uuid

class LoanService:
    def __init__(self, customer_id, principal, rate, term_years):
        # Store customer loan details
        self.loan_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.principal = principal  # loan amount
        self.rate = rate            # interest rate (e.g., 0.05 for 5%)
        self.term = term_years     # duration in years

    def calculate_interest(self):
        # Simple interest formula: P * R * T
        interest = self.principal * self.rate * self.term
        return self.principal + interest

    def calculate_total_payable(self):
        # Returns the total amount to be repaid (principal + interest)
        return self.calculate_interest()

    def to_dict(self):
        # Convert to dictionary for saving
        return {
            "loan_id": self.loan_id,
            "customer_id": self.customer_id,
            "principal": self.principal,
            "rate": self.rate,
            "term": self.term,
            "total_payable": self.calculate_total_payable()
        }