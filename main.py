import json
from models.customer import Customer
from models.account import Account
from models.services import LoanService

# Location of JSON file to store all data
DATA_FILE = "data/bank_data.json"

def load_data():
    # Load all customer, account, and employee data from JSON file
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Return empty data structure if file doesn't exist
        return {"customers": [], "accounts": [], "employees": []}

def save_data(data):
    # Save all data back to the JSON file with proper indentation
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def create_customer():
    # Input user details to create a new customer
    fname = input("First name: ")
    lname = input("Last name: ")
    addr = input("Address: ")
    customer = Customer(fname, lname, addr)

    # Load existing data, add new customer, save it
    data = load_data()
    data["customers"].append(customer.to_dict())
    save_data(data)
    print("✅ Customer created successfully!")

def create_account():
    # Create new account linked to an existing customer
    cust_id = input("Enter customer ID: ")
    acc_type = input("Account Type (checking/savings/loan): ")
    account = Account(cust_id, acc_type)

    # Add account to data store
    data = load_data()
    data["accounts"].append(account.to_dict())
    save_data(data)
    print("✅ Account created!")

def view_customer_accounts():
    # Ask for the customer's ID
    cust_id = input("Enter customer ID: ")

    data = load_data()
    found = False  # Flag to check if any accounts are found

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


def create_loan():
    # Input loan details from user
    cust_id = input("Customer ID: ")
    principal = float(input("Loan amount: "))
    rate = float(input("Annual interest rate (e.g., 0.05): "))
    term = int(input("Loan term in years: "))

    # Create LoanService object and store it
    loan = LoanService(cust_id, principal, rate, term)
    
    data = load_data()
    data["loans"].append(loan.to_dict())
    save_data(data)

    print(f"✅ Loan created! Total to repay: ${loan.calculate_total_payable():,.2f}")


def view_customers():
    # Display all existing customers with their names and IDs
    data = load_data()
    for cust in data["customers"]:
        print(f'{cust["first_name"]} {cust["last_name"]} - ID: {cust["customer_id"]}')

def view_loans():
    data = load_data()
    for loan in data["loans"]:
        print(f"Loan ID: {loan['loan_id']} | Customer: {loan['customer_id']} | Repay: ${loan['total_payable']:,.2f}")



def main():
    # Main CLI menu loop
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
