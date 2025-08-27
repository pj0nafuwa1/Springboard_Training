from pathlib import Path

def analyze_file(file_path):
    error_count = 0
    error_lines = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if 'ERROR' in line:
                error_count += 1
                error_lines.append(line.strip())
    return error_count, error_lines

def main():
    log_dir = '../logs'  # Path to the Airflow logs directory (relative to airflow_docker/log_analyzer)
    total_errors = 0
    all_error_lines = []

    for log_file in Path(log_dir).rglob('*.log'):
        count, errors = analyze_file(log_file)
        total_errors += count
        all_error_lines.extend(errors)

    print(f"Total error messages found: {total_errors}")
    print("Error details:")
    for error in all_error_lines:
        print(error)

if __name__ == '__main__':
    main()
