"""
utils.py
Common file-handling helper functions used across all modules.
Employee record format in employees.txt (fields separated by '|'):
    EmpID|Name|Department|BasicSalary|BonusPercent
Attendance record format in attendance.txt:
    EmpID|Date|Status
"""

import os

DATA_DIR = "data"
EMPLOYEE_FILE = os.path.join(DATA_DIR, "employees.txt")
ATTENDANCE_FILE = os.path.join(DATA_DIR, "attendance.txt")
ADMIN_FILE = os.path.join(DATA_DIR, "admin.txt")


def ensure_data_files():
    """Create data folder and files (with a default admin account) if missing."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(EMPLOYEE_FILE):
        open(EMPLOYEE_FILE, "w").close()

    if not os.path.exists(ATTENDANCE_FILE):
        open(ATTENDANCE_FILE, "w").close()

    if not os.path.exists(ADMIN_FILE):
        with open(ADMIN_FILE, "w") as f:
            f.write("admin|admin123\n")  # default username/password


def read_lines(filepath):
    """Read all non-empty lines from a file and return as a list of stripped strings."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]


def write_lines(filepath, lines):
    """Overwrite a file with the given list of lines."""
    with open(filepath, "w") as f:
        for line in lines:
            f.write(line + "\n")


def append_line(filepath, line):
    """Append a single line to a file."""
    with open(filepath, "a") as f:
        f.write(line + "\n")


def get_all_employees():
    """Return list of employee records as dictionaries."""
    employees = []
    for line in read_lines(EMPLOYEE_FILE):
        parts = line.split("|")
        if len(parts) == 5:
            employees.append({
                "id": parts[0],
                "name": parts[1],
                "department": parts[2],
                "salary": float(parts[3]),
                "bonus": float(parts[4]),
            })
    return employees


def save_all_employees(employees):
    """Save a list of employee dictionaries back to the file."""
    lines = [
        f"{e['id']}|{e['name']}|{e['department']}|{e['salary']}|{e['bonus']}"
        for e in employees
    ]
    write_lines(EMPLOYEE_FILE, lines)


def find_employee_by_id(emp_id):
    """Return employee dict if found, else None."""
    for e in get_all_employees():
        if e["id"] == emp_id:
            return e
    return None
