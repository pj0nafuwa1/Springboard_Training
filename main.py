import json
import logging
from models.customer import Customer
from models.account import Account
from models.services import LoanService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler('logs/banking.log'),
        logging.StreamHandler()
    ]
)

# Location of JSON file to store all data
DATA_FILE = "data/bank_data.json"

def load_data():
    """Load all customer, account, and employee data from JSON file."""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning("Data file not found. Returning empty data structure.")
        return {"customers": [], "accounts": [], "employees": [], "loans": []}
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return {"customers": [], "accounts": [], "employees": [], "loans": []}

def save_data(data):
    """Save all data back to the JSON file with proper indentation."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"Error saving data: {e}")

def create_customer():
    """Create a new customer from user input."""
    try:
        fname = input("First name: ")
        lname = input("Last name: ")
        addr = input("Address: ")
        customer = Customer(fname, lname, addr)
        data = load_data()
        data["customers"].append(customer.to_dict())
        save_data(data)
        logging.info("Customer created successfully!")
        print("✅ Customer created successfully!")
    except Exception as e:
        logging.error(f"Error creating customer: {e}")
        print("❌ Error creating customer.")

def create_account():
    """Create a new account linked to an existing customer."""
    try:
        cust_id = input("Enter customer ID: ")
        acc_type = input("Account Type (checking/savings/loan): ")
        account = Account(cust_id, acc_type)
        data = load_data()
        data["accounts"].append(account.to_dict())
        save_data(data)
        logging.info("Account created!")
        print("✅ Account created!")
    except Exception as e:
        logging.error(f"Error creating account: {e}")
        print("❌ Error creating account.")

def view_customer_accounts():
    """Display all accounts for a given customer ID."""
    try:
        cust_id = input("Enter customer ID: ")
        data = load_data()
        found = False
        print(f"\n📂 Accounts for Customer ID: {cust_id}")
        print("-" * 40)
        for acc in data["accounts"]:
            if acc["customer_id"] == cust_id:
                found = True
                print(f"Account ID:    {acc['account_id']}")
                print(f"Account Type:  {acc['account_type']}")
                print(f"Balance:       ${acc['balance']:,.2f}")
                print("-" * 40)
        if not found:
            print("❌ No accounts found for this customer ID.")
    except Exception as e:
        logging.error(f"Error viewing customer accounts: {e}")
        print("❌ Error viewing accounts.")

def create_loan():
    """Create a new loan for a customer."""
    try:
        cust_id = input("Customer ID: ")
        principal = float(input("Loan amount: "))
        rate = float(input("Annual interest rate (e.g., 0.05): "))
        term = int(input("Loan term in years: "))
        loan = LoanService(cust_id, principal, rate, term)
        data = load_data()
        data["loans"].append(loan.to_dict())
        save_data(data)
        logging.info("Loan created!")
        print(f"✅ Loan created! Total to repay: ${loan.calculate_total_payable():,.2f}")
    except Exception as e:
        logging.error(f"Error creating loan: {e}")
        print("❌ Error creating loan.")

def view_customers():
    """Display all existing customers with their names and IDs."""
    try:
        data = load_data()
        for cust in data["customers"]:
            print(f'{cust["first_name"]} {cust["last_name"]} - ID: {cust["customer_id"]}')
    except Exception as e:
        logging.error(f"Error viewing customers: {e}")
        print("❌ Error viewing customers.")

def view_loans():
    """Display all loans in the system."""
    try:
        data = load_data()
        for loan in data["loans"]:
            print(f"Loan ID: {loan['loan_id']} | Customer: {loan['customer_id']} | Repay: ${loan['total_payable']:,.2f}")
    except Exception as e:
        logging.error(f"Error viewing loans: {e}")
        print("❌ Error viewing loans.")

def main():
    """Main CLI menu loop for the banking system."""
    while True:
        print("\n--- BANKING SYSTEM ---")
        print("1. Create Customer")
        print("2. View Customers")
        print("3. Create Account")
        print("4. View Account")
        print("5. Create Loan")
        print("6. View Loans")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            create_account()
        elif choice == '4':
            view_customer_accounts()
        elif choice == '5':
            create_loan()
        elif choice == '6':
            view_loans()
        elif choice == '7':
            print("Thank you for you business. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    # This block ensures main() only runs when this script is executed directly
    main()
