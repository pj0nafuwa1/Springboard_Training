


# Ticket Sales Data Loader and Analyzer

## Table of Contents
- About The Project
- Getting Started
- Usage
- Contributing
- License
- Contact
- Acknowledgements

## About The Project
This project provides a simple way to load ticket sales data from a CSV file into a SQLite database and analyze the most popular events for the past month. It consists of two scripts:

- `ticket_sales_table_setup.py`: Sets up the `ticket_sales` table and loads data from a CSV file (no headers, 10 columns per row).
- `mini_project_ticketing.py`: Analyzes the loaded data and displays the top-selling events for the past month, with recommendations.

### Built With
- Python 3.x
- SQLite (via Python's built-in sqlite3 module)

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/<your-username>/<your-repo-name>.git
   ```
2. Place your ticket sales CSV file(s) in the `data` folder. Each row must have 10 columns in the order below, with no header row:
   - ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets

## Usage
1. Run the setup script to load data:
   ```sh
   python models/ticketing/ticket_sales_table_setup.py
   ```
   - Select the CSV file to load when prompted.
2. Run the analysis script to display results:
   ```sh
   python models/ticketing/mini_project_ticketing.py
   ```

### Example CSV Row
```
1,20250801,101,Concert A,20250815,Music,Lagos,501,150.00,2
```

This row will be loaded as:
- ticket_id: 1
- trans_date: 20250801
- event_id: 101
- event_name: Concert A
- event_date: 20250815
- event_type: Music
- event_city: Lagos
- customer_id: 501
- price: 150.00
- num_tickets: 2

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Your Name - ponafuwa@hotmail.com
Project Link: https://github.com/pj0nafuwa1/Springboard_Training

## Acknowledgements
- [PurpleBooth README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python csv Module](https://docs.python.org/3/library/csv.html)
