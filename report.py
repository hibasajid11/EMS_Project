"""
report.py
Report Module - Total employees, employees in each department,
highest-salaried employee, lowest-salaried employee.
"""

from utils import get_all_employees


def generate_report():
    print("\n===== EMPLOYEE REPORT =====")
    employees = get_all_employees()

    if not employees:
        print("No employee records found.\n")
        return

    # Total employees
    print(f"Total Employees: {len(employees)}")

    # Employees in each department
    departments = {}
    for e in employees:
        departments[e["department"]] = departments.get(e["department"], 0) + 1

    print("\nEmployees per Department:")
    for dept, count in departments.items():
        print(f"  {dept}: {count}")

    # Highest and lowest salaried employee
    highest = max(employees, key=lambda e: e["salary"])
    lowest = min(employees, key=lambda e: e["salary"])

    print(f"\nHighest Salaried Employee: {highest['name']} (ID: {highest['id']}) - {highest['salary']}")
    print(f"Lowest Salaried Employee: {lowest['name']} (ID: {lowest['id']}) - {lowest['salary']}\n")
