
# Ticket Sales Table Setup Script
# This script creates the ticket_sales table and loads data from a CSV file (no headers, 10 columns per row).

import sqlite3
import csv
import os

# Database and data directory configuration
DB_FILE = "ticket_sales.db"
DATA_DIR = r"C:\Users\POnaf\SpringBoard\data"

def setup_database():
    """
    Drops the existing ticket_sales table (if any) and creates a new one with the required schema.
    Returns the database connection and cursor.
    """
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    # Drop table if it exists to ensure schema is correct
    cur.execute("DROP TABLE IF EXISTS ticket_sales;")
    # Create table with specified columns
    cur.execute("""
        CREATE TABLE ticket_sales (
            ticket_id INTEGER,
            trans_date DATE,
            event_id INTEGER,
            event_name VARCHAR(50),
            event_date DATE,
            event_type VARCHAR(10),
            event_city VARCHAR(20),
            customer_id INTEGER,
            price DECIMAL,
            num_tickets INTEGER
        )
    """)
    conn.commit()
    return conn, cur

def load_csv_to_db(cur, conn, csv_path):
    """
    Loads data from a CSV file into the ticket_sales table.
    Assumes no header row and exactly 10 columns per row.
    Skips rows with incorrect column count.
    """
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        print("Ingesting CSV data by position (no headers)...")
        for row in reader:
            if len(row) != 10:
                print(f"Skipping row with unexpected number of columns: {row}")
                continue
            # Insert row into ticket_sales table
            cur.execute("""
                INSERT INTO ticket_sales (ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                int(row[0]),      # ticket_id
                row[1],           # trans_date
                int(row[2]),      # event_id
                row[3],           # event_name
                row[4],           # event_date
                row[5],           # event_type
                row[6],           # event_city
                int(row[7]),      # customer_id
                float(row[8]),    # price
                int(row[9])       # num_tickets
            ))
    conn.commit()

if __name__ == "__main__":
    # List available CSV files in the data directory
    files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
    if not files:
        print("No CSV files found in the data directory.")
        exit(1)
    print("Available CSV files:")
    for idx, fname in enumerate(files):
        print(f"{idx+1}. {fname}")
    # Prompt user to select a file
    choice = input("Select a file by number: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(files):
            selected_file = files[idx]
        else:
            print("Invalid selection. Using first file.")
            selected_file = files[0]
    except Exception:
        print("Invalid input. Using first file.")
        selected_file = files[0]
    # Setup database and load selected CSV file
    conn, cur = setup_database()
    csv_path = os.path.join(DATA_DIR, selected_file)
    load_csv_to_db(cur, conn, csv_path)
    conn.close()
