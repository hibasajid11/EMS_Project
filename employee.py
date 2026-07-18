"""
employee.py
Employee Management Module - Add, View, Update, Delete employee records.
"""

from utils import get_all_employees, save_all_employees, find_employee_by_id, append_line, EMPLOYEE_FILE


def add_employee():
    print("\n----- Add Employee -----")
    emp_id = input("Employee ID: ").strip()

    if find_employee_by_id(emp_id):
        print("An employee with this ID already exists.\n")
        return

    name = input("Name: ").strip()
    department = input("Department: ").strip()

    try:
        salary = float(input("Basic Salary: ").strip())
        bonus = float(input("Bonus Percent (e.g. 10 for 10%): ").strip())
    except ValueError:
        print("Invalid number entered. Employee not added.\n")
        return

    line = f"{emp_id}|{name}|{department}|{salary}|{bonus}"
    append_line(EMPLOYEE_FILE, line)
    print(f"Employee '{name}' added successfully.\n")


def view_employees():
    employees = get_all_employees()
    print("\n----- All Employees -----")

    if not employees:
        print("No employee records found.\n")
        return

    print(f"{'ID':<8}{'Name':<15}{'Department':<15}{'Salary':<10}{'Bonus%':<8}")
    print("-" * 56)
    for e in employees:
        print(f"{e['id']:<8}{e['name']:<15}{e['department']:<15}{e['salary']:<10}{e['bonus']:<8}")
    print()


def update_employee():
    print("\n----- Update Employee -----")
    emp_id = input("Enter Employee ID to update: ").strip()
    employees = get_all_employees()

    for e in employees:
        if e["id"] == emp_id:
            print(f"Current details -> Name: {e['name']}, Department: {e['department']}, "
                  f"Salary: {e['salary']}, Bonus%: {e['bonus']}")

            new_name = input(f"New Name (leave blank to keep '{e['name']}'): ").strip()
            new_dept = input(f"New Department (leave blank to keep '{e['department']}'): ").strip()
            new_salary = input(f"New Salary (leave blank to keep {e['salary']}): ").strip()
            new_bonus = input(f"New Bonus% (leave blank to keep {e['bonus']}): ").strip()

            if new_name:
                e["name"] = new_name
            if new_dept:
                e["department"] = new_dept
            if new_salary:
                try:
                    e["salary"] = float(new_salary)
                except ValueError:
                    print("Invalid salary, keeping old value.")
            if new_bonus:
                try:
                    e["bonus"] = float(new_bonus)
                except ValueError:
                    print("Invalid bonus, keeping old value.")

            save_all_employees(employees)
            print("Employee updated successfully.\n")
            return

    print("Employee not found.\n")


def delete_employee():
    print("\n----- Delete Employee -----")
    emp_id = input("Enter Employee ID to delete: ").strip()
    employees = get_all_employees()

    updated = [e for e in employees if e["id"] != emp_id]

    if len(updated) == len(employees):
        print("Employee not found.\n")
        return

    confirm = input(f"Are you sure you want to delete employee {emp_id}? (y/n): ").strip().lower()
    if confirm == "y":
        save_all_employees(updated)
        print("Employee deleted successfully.\n")
    else:
        print("Delete cancelled.\n")
