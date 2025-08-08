import sqlite3
import csv
import os
from datetime import datetime, timedelta

DB_FILE = "ticket_sales.db"
DATA_DIR = "data"
CSV_FILE = "third_party_sales_1.csv"

# 1. Setup database connection and create sales table
def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            ticket_type TEXT NOT NULL,
            sale_date TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    return conn, cur

# 2. Load the CSV file into the table
def load_csv_to_db(cur, conn, csv_path):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
                INSERT INTO sales (event_name, ticket_type, sale_date, quantity, price)
                VALUES (?, ?, ?, ?, ?)
            """, (
                row['event_name'],
                row['ticket_type'],
                row['sale_date'],
                int(row['quantity']),
                float(row['price'])
            ))
    conn.commit()

# 3. Display statistical information (top-selling events in the past month)
def get_top_selling_events(cur):
    one_month_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    cur.execute("""
        SELECT event_name, SUM(quantity) as total_tickets
        FROM sales
        WHERE sale_date >= ?
        GROUP BY event_name
        ORDER BY total_tickets DESC
        LIMIT 5
    """, (one_month_ago,))
    return cur.fetchall()

# 4. Display results in user-friendly format
def display_results(results):
    print("\nTop-Selling Events in the Past Month:")
    print("{:<30} {:>15}".format("Event Name", "Tickets Sold"))
    print("-" * 45)
    for event, tickets in results:
        print("{:<30} {:>15}".format(event, tickets))

if __name__ == "__main__":
    conn, cur = setup_database()
    csv_path = os.path.join(DATA_DIR, CSV_FILE)
    load_csv_to_db(cur, conn, csv_path)
    results = get_top_selling_events(cur)
    display_results(results)
    conn.close()
