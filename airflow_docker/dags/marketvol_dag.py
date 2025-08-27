
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import yfinance as yf
import pandas as pd
from datetime import date
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Set the start date to today at 6 PM
start_date = datetime.combine(datetime.today(), datetime.min.time()).replace(hour=18)

with DAG(
    'marketvol',
    default_args=default_args,
    description='A simple DAG',
    schedule='0 18 * * 1-5',  # 6 PM, Mon-Fri
    start_date=start_date,
    catchup=True,
    tags=['market', 'yfinance'],
) as dag:
    # Task task0: Create a temp directory for the execution date
    task0 = BashOperator(
        task_id='create_temp_dir',
        bash_command='mkdir -p /tmp/data/{{ ds }}',
    )

    def download_stock_data(symbol, execution_date, **kwargs):
        start_date = pd.to_datetime(execution_date)
        end_date = start_date + pd.Timedelta(days=1)
        df = yf.download(symbol, start=start_date, end=end_date, interval='1m')
        output_path = f"/tmp/data/{execution_date}/{symbol}.csv"
        df.to_csv(output_path, header=False)

    task1 = PythonOperator(
        task_id='download_aapl',
        python_callable=download_stock_data,
        op_kwargs={'symbol': 'AAPL', 'execution_date': '{{ ds }}'},
    )

    task2 = PythonOperator(
        task_id='download_tsla',
        python_callable=download_stock_data,
        op_kwargs={'symbol': 'TSLA', 'execution_date': '{{ ds }}'},
    )

    # Directory to move files to (can be changed as needed)
    data_dir = '/tmp/market_data/{{ ds }}'

    task3 = BashOperator(
        task_id='move_aapl',
        bash_command='mkdir -p ' + data_dir + ' && mv /tmp/data/{{ ds }}/AAPL.csv ' + data_dir + '/',
    )

    task4 = BashOperator(
        task_id='move_tsla',
        bash_command='mkdir -p ' + data_dir + ' && mv /tmp/data/{{ ds }}/TSLA.csv ' + data_dir + '/',
    )

    def run_custom_query(execution_date, **kwargs):
        data_dir = f"/tmp/market_data/{execution_date}"
        aapl_path = f"{data_dir}/AAPL.csv"
        tsla_path = f"{data_dir}/TSLA.csv"
        # Example: Read both CSVs and print the number of rows in each
        aapl_df = pd.read_csv(aapl_path, header=None)
        tsla_df = pd.read_csv(tsla_path, header=None)
        print(f"AAPL rows: {len(aapl_df)}")
        print(f"TSLA rows: {len(tsla_df)}")
        # Add your custom query logic here

    task5 = PythonOperator(
        task_id='run_query',
        python_callable=run_custom_query,
        op_kwargs={'execution_date': '{{ ds }}'},
    )

    # Set task dependencies
    task0 >> [task1, task2]
    task1 >> task3
    task2 >> task4
    [task3, task4] >> task5
