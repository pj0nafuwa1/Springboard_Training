# Airflow Log Analyzer

This project provides a simple Python tool to analyze Airflow log files and report error messages in an easy-to-read format. It is designed to help you monitor your Airflow DAGs and quickly identify any issues.

## Getting Started

### Prerequisites
- Airflow logs available from your previous Airflow mini-project

### Installation
1. Clone this repository (https://github.com/pj0nafuwa1/Springboard_Training/tree/dev/airfow_docker/log_analyzer) or download the `log_analyzer` directory to your local machine.
2. Ensure your Airflow logs are available in the `../logs` directory relative to the `log_analyzer` folder. Adjust the path in the script if your logs are elsewhere.

### Usage
1. Open a terminal and navigate to the `log_analyzer` directory:
   ```
   cd airflow_docker/log_analyzer
   ```
2. Run the log analyzer script:
   ```
   python airflow_log_analyzer.py
   ```
3. The script will print:
   - The total number of error messages found in all Airflow log files
   - The details of each error message

### Example Output
```
Total error messages found: 2
Error details:
2025-08-22 18:01:23,456 ERROR - Task failed due to ...
2025-08-22 18:02:10,789 ERROR - Connection timeout ...
```

### Verifying Results
- Check that the total error count matches the number of error lines in your log files.
- Review the error details printed to the console for troubleshooting.

### Example Log
See `log_analyzer.txt` for a sample command line execution log.

## Authors
- Adepeju Onafuwa

## Acknowledgments
- [PurpleBooth README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
