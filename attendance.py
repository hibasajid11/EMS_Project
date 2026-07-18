"""
attendance.py
Attendance Module - Mark attendance, view attendance record,
count present/absent days.
Record format in attendance.txt: EmpID|Date|Status
"""

from datetime import date
from utils import read_lines, append_line, find_employee_by_id, ATTENDANCE_FILE


def mark_attendance():
    print("\n----- Mark Attendance -----")
    emp_id = input("Enter Employee ID: ").strip()

    if not find_employee_by_id(emp_id):
        print("Employee not found.\n")
        return

    today = str(date.today())
    status = input("Status (P = Present, A = Absent): ").strip().upper()

    if status not in ("P", "A"):
        print("Invalid status. Use P or A.\n")
        return

    status_word = "Present" if status == "P" else "Absent"
    append_line(ATTENDANCE_FILE, f"{emp_id}|{today}|{status_word}")
    print(f"Attendance marked: {status_word} on {today}.\n")


def view_attendance():
    print("\n----- View Attendance Record -----")
    emp_id = input("Enter Employee ID: ").strip()

    records = [line for line in read_lines(ATTENDANCE_FILE) if line.split("|")[0] == emp_id]

    if not records:
        print("No attendance records found for this employee.\n")
        return

    print(f"{'Date':<15}{'Status':<10}")
    print("-" * 25)
    for line in records:
        _, rec_date, status = line.split("|")
        print(f"{rec_date:<15}{status:<10}")
    print()


def count_attendance():
    print("\n----- Present/Absent Count -----")
    emp_id = input("Enter Employee ID: ").strip()

    records = [line for line in read_lines(ATTENDANCE_FILE) if line.split("|")[0] == emp_id]

    if not records:
        print("No attendance records found for this employee.\n")
        return

    present = sum(1 for line in records if line.split("|")[2] == "Present")
    absent = sum(1 for line in records if line.split("|")[2] == "Absent")

    print(f"Present days: {present}")
    print(f"Absent days: {absent}\n")
