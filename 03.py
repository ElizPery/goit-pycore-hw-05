import argparse
from collections import defaultdict
from pathlib import Path

# Add parser of arguments in terminal
parser = argparse.ArgumentParser(description="Path to file with logs")
parser.add_argument("--filepath", required=True)
parser.add_argument("--loglevel")
args = parser.parse_args()

# Function that takes line of the log and return this data converted in dict
def parse_log_line(line: str) -> dict:
    date, time, level, *args = line.split()
    dictionary = {'date': date, 'time': time, 'level': level, 'details': ' '.join(args)}
    return dictionary

# Function that takes path to the file with log data and return list of parsed data using func parse_log_line
# If file missed or not existed print exeption and return None
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()

            return [parse_log_line(line) for line in data]
    except:
        print('Data have lost or inaccurate, please try again and check data file')
        return None
    
# Function that takes list of dict with logs data and name of level, return filtered list of certain name of log level
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

# Function that takes list of dict with logs data and return dict where key is name of log level, and value is number of logs with this name
def count_logs_by_level(logs: list) -> dict:
    logs_by_level = defaultdict(int)
    for log in logs:
        if log['level'] in logs_by_level:
            logs_by_level[log['level']] += 1
        else:
            logs_by_level[log['level']] = 1
    return dict(logs_by_level)

# Function that takes dict where key is name of log level, and value is number of logs with this name, and print decorated data
def display_log_counts(counts: dict):
    list_of_str = []
    for key, value in counts.items():
        list_of_str.append(f'{key:<17}|{value:<10}\n')
    print(f'\nРівень логування | Кількість\n{'-'*27}\n{''.join(list_of_str)}')

def main():
    # Declare variables to identify args
    file_path = Path(__file__).parent / args.filepath
    logs_level = args.loglevel

    # list of parsed data
    logs = load_logs(file_path)

    # If not None continue operations
    if(logs):
        dictionary_logs = count_logs_by_level(logs)
        display_log_counts(dictionary_logs)

        # If was writen logs level print data about it
        if (logs_level):
            list_logs = filter_logs_by_level(logs, logs_level)
            list_of_str = []
            for log in list_logs:
                list_of_str.append(f'{log['date']} {log['time']} - {log['details']}\n')
            print(f'Деталі логів для рівня {logs_level.upper()}:\n{''.join(list_of_str)}')

    
if __name__ == '__main__':
    main()