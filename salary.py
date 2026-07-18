"""
salary.py
Salary Management Module (simplified) - Set salary, set bonus percent,
calculate net salary = basic salary + (basic salary * bonus% / 100)
"""

from utils import get_all_employees, save_all_employees, find_employee_by_id


def set_salary():
    print("\n----- Set Salary / Bonus -----")
    emp_id = input("Enter Employee ID: ").strip()
    employee = find_employee_by_id(emp_id)

    if not employee:
        print("Employee not found.\n")
        return

    try:
        salary = float(input(f"New Basic Salary (current: {employee['salary']}): ").strip())
        bonus = float(input(f"New Bonus Percent (current: {employee['bonus']}): ").strip())
    except ValueError:
        print("Invalid number entered.\n")
        return

    employees = get_all_employees()
    for e in employees:
        if e["id"] == emp_id:
            e["salary"] = salary
            e["bonus"] = bonus
            break

    save_all_employees(employees)
    print("Salary details updated successfully.\n")


def calculate_net_salary():
    print("\n----- Calculate Net Salary -----")
    emp_id = input("Enter Employee ID: ").strip()
    employee = find_employee_by_id(emp_id)

    if not employee:
        print("Employee not found.\n")
        return

    bonus_amount = employee["salary"] * employee["bonus"] / 100
    net_salary = employee["salary"] + bonus_amount

    print(f"\nEmployee: {employee['name']}")
    print(f"Basic Salary: {employee['salary']}")
    print(f"Bonus ({employee['bonus']}%): {bonus_amount:.2f}")
    print(f"Net Salary: {net_salary:.2f}\n")
