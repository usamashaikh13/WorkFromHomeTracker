from app.tracker import WorkFromHomeTracker
from datetime import datetime

if __name__ == '__main__':
    # Create an instance of the WorkFromHomeTracker
    tracker = WorkFromHomeTracker('data/work_hours.csv')

    # Log work hours for employees
    tracker.log_work_hours('001', datetime(2023, 10, 1, 9, 0), datetime(2023, 10, 1, 17, 0))
    tracker.log_work_hours('002', datetime(2023, 10, 1, 8, 30), datetime(2023, 10, 1, 16, 30))

    # Generate and print a report for all employees
    report = tracker.generate_report()
    for entry in report:
        print(entry)
