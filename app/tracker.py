import csv
from datetime import datetime

class WorkFromHomeTracker:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.records = self.load_records()

    def load_records(self):
        """Load records from the CSV file."""
        records = []
        with open(self.csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                records.append(row)
        return records

    def log_work_hours(self, employee_id, start_time, end_time):
        """Log work hours for an employee.

        Args:
            employee_id (str): The Employee ID.
            start_time (datetime): The start time of work.
            end_time (datetime): The end time of work.
        """
        with open(self.csv_file, 'a', newline='') as file:
            fieldnames = ['Employee ID', 'Start Time', 'End Time']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writerow({
                'Employee ID': employee_id,
                'Start Time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
                'End Time': end_time.strftime('%Y-%m-%d %H:%M:%S')
            })

    def generate_report(self):
        """Generate a report of work hours for all employees.

        Returns:
            list: A list of work hour records.
        """
        return self.records
