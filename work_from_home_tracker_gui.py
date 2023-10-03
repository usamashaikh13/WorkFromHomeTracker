import tkinter as tk
from tkinter import ttk
from app.tracker import WorkFromHomeTracker
from datetime import datetime

class WorkFromHomeTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Work From Home Tracker")
        self.tracker = WorkFromHomeTracker('data/work_hours.csv')

        # Create and set up widgets
        ttk.Label(root, text="Employee ID:").grid(row=0, column=0)
        self.employee_id_entry = ttk.Entry(root)
        self.employee_id_entry.grid(row=0, column=1)

        ttk.Label(root, text="Start Time:").grid(row=1, column=0)
        self.start_time_entry = ttk.Entry(root)
        self.start_time_entry.grid(row=1, column=1)

        ttk.Label(root, text="End Time:").grid(row=2, column=0)
        self.end_time_entry = ttk.Entry(root)
        self.end_time_entry.grid(row=2, column=1)

        self.log_button = ttk.Button(root, text="Log Work Hours", command=self.log_work_hours)
        self.log_button.grid(row=3, column=0, columnspan=2)

        self.generate_report_button = ttk.Button(root, text="Generate Report", command=self.generate_report)
        self.generate_report_button.grid(row=4, column=0, columnspan=2)

        self.report_text = tk.Text(root, height=10, width=40)
        self.report_text.grid(row=5, column=0, columnspan=2)

    def log_work_hours(self):
        employee_id = self.employee_id_entry.get()
        start_time_str = self.start_time_entry.get()
        end_time_str = self.end_time_entry.get()

        try:
            start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
            self.tracker.log_work_hours(employee_id, start_time, end_time)
            self.report_text.insert(tk.END, f"Logged work hours for Employee ID: {employee_id}\n")
        except ValueError:
            self.report_text.insert(tk.END, "Invalid date/time format. Please use YYYY-MM-DD HH:MM:SS\n")

    def generate_report(self):
        self.report_text.delete(1.0, tk.END)
        report = self.tracker.generate_report()
        for entry in report:
            self.report_text.insert(tk.END, f"Employee ID: {entry['Employee ID']}, "
                                            f"Start Time: {entry['Start Time']}, "
                                            f"End Time: {entry['End Time']}\n")

if __name__ == '__main__':
    root = tk.Tk()
    app = WorkFromHomeTrackerGUI(root)
    root.mainloop()
