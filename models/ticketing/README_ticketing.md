# Mini Project: Ticket Sales Data Loader and Analyzer

## Overview
This project loads ticket sales data from a CSV file into a SQLite database, analyzes top-selling events for the past month, and displays results in a user-friendly format.

## Prerequisites
- Python 3.x
- No external dependencies required (uses built-in `sqlite3` and `csv` modules)

## Files
- `mini_project_ticketing.py`: Main script
- `data/third_party_sales_1.csv`: Source data file

## How to Run
1. Ensure you have Python 3 installed.
2. Place `third_party_sales_1.csv` in the `data` folder.
3. Run the script:
   ```
   python mini_project_ticketing.py
   ```
4. The script will:
   - Create a SQLite database and sales table
   - Load data from the CSV file
   - Display the top-selling events for the past month

## Output
Results are displayed in a formatted table showing the most popular events by ticket sales.

## Customization
- To analyze a different CSV file, update the `CSV_FILE` variable in `mini_project_ticketing.py`.
- The database file is named `ticket_sales.db` and is created in the project folder.

## Recommendations
After loading the data, the script recommends popular events based on ticket sales for the past month.
