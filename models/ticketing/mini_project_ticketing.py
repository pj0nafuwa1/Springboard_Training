import sqlite3
import csv
import os
from datetime import datetime, timedelta


# Database file configuration
DB_FILE = "ticket_sales.db"

def list_csv_files():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
    return files

def prompt_for_csv_file(files):
    print("Available CSV files:")
    for idx, fname in enumerate(files):
        print(f"{idx+1}. {fname}")
    choice = input("Select a file by number: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(files):
            return files[idx]
        else:
            print("Invalid selection. Using first file.")
            return files[0]
    except Exception:
        print("Invalid input. Using first file.")
        return files[0]

# 1. Setup database connection and create sales table
def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    # No table creation here; assumes ticket_sales_table_setup.py has already created and loaded the table
    conn.commit()
    return conn, cur

# 2. Load the CSV file into the table
def load_csv_to_db(cur, conn, csv_path):
    pass  # Data loading is handled by ticket_sales_table_setup.py

# 3. Display statistical information (top-selling events in the past month)

def get_top_selling_events(cur):
    """
    Query the ticket_sales table for the top-selling events in the past month.
    Returns a list of (event_name, total_tickets) tuples.
    """
    one_month_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    cur.execute("""
        SELECT event_name, SUM(num_tickets) as total_tickets
        FROM ticket_sales
        WHERE event_date >= ?
        GROUP BY event_name
        ORDER BY total_tickets DESC
        LIMIT 5
    """, (one_month_ago,))
    return cur.fetchall()

# 4. Display results in user-friendly format

def display_results(results):
    """
    Display the top-selling events in a user-friendly table format and provide recommendations.
    """
    print("\nHere are the most popular events in the past month:")
    for event, _ in results:
        print("- {}".format(event))
    if results:
        print("\nRecommendation: Consider focusing marketing efforts on these popular events to maximize ticket sales.")
    else:
        print("No ticket sales found for the past month.")


if __name__ == "__main__":
    # Connect to the database
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    # Query for top-selling events
    results = get_top_selling_events(cur)
    # Display results and recommendations
    display_results(results)
    # Close the database connection
    conn.close()
