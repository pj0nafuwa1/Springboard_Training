# Banking System Project

## Overview
This is a simple command-line banking system implemented in Python. It allows you to create customers, accounts, and loans, and view all records. Data is stored in a JSON file. The project follows PEP-8, is well-documented, and includes logging and exception handling.

## Features
- Create and view customers
- Create and view accounts
- Create and view loans
- Data persistence in JSON
- Logging to both console and file (`logs/banking.log`)
- Graceful error handling

## How to Run
1. Run the program:
   ```
   python main.py
   ```
2. Follow the on-screen menu to interact with the system.

## Logging
- All actions and errors are logged to `logs/banking.log`.
- Errors and warnings are also printed to the screen.

## Project Structure
- `main.py`: Main CLI and logic
- `models/`: Contains `customer.py`, `account.py`, `employee.py`, `services.py`
- `data/bank_data.json`: Data storage
- `logs/banking.log`: Log file

## UML Diagram
See `UML.md` for a class diagram.

## Exception Handling
- All user input and file operations are wrapped in try/except blocks.
- Errors are logged and displayed to the user.

## PEP-8 & Documentation
- All code is formatted to PEP-8 standards.
- Each class and function includes docstrings and comments.
