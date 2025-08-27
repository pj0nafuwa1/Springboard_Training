# Project Title

Airflow Stock Market Data Pipeline

## Description
This project uses Apache Airflow to automatically download, process, and analyze stock market data for Apple (AAPL) and Tesla (TSLA) from Yahoo Finance. The workflow is scheduled to run every weekday at 6 PM, saving the data and running a simple analysis. The project is designed for easy setup and use, even for those without a technical background.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your computer
- Git installed

### Installation
1. Clone this repository:
   ```
   git clone https://github.com/pj0nafuwa1/Springboard_Training/tree/dev
   ```
2. Ensure Docker Desktop is running.
3. In the `airfow_docker` directory, make sure the following files exist:
   - `dags/marketvol_dag.py` (the Airflow DAG)
   - `requirements.txt` (contains `yfinance` and `pandas`)
   - `docker-compose.yaml` (Airflow setup)

### Usage
1. Start Airflow and its services:
   ```
   docker-compose up -d
   ```
2. Open your browser and go to (http://localhost:8080)
   - Login with username: `airflow`, password: `airflow` (default)
3. Find the `marketvol` DAG in the list and enable it (toggle the switch).
4. You can trigger a run manually by clicking the play button, or wait for the scheduled time (6 PM on weekdays).
5. Monitor the progress and logs in the Airflow UI.

### Verifying Results
- The downloaded data and results will be saved in the `/tmp/market_data/<date>/` directory inside the Airflow container.
- You can view task logs in the Airflow UI for details about each step.

## Built With
- Apache Airflow(https://airflow.apache.org/)
- Docker(https://www.docker.com/)
- yfinance(https://pypi.org/project/yfinance/)
- pandas(https://pandas.pydata.org/)

## Authors
- Adepeju Onafuwa

## Acknowledgments
- [PurpleBooth README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)

## Example Log
See `example_run_log.txt` for a sample of a successful job run.
