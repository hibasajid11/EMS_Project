"""
department.py
Department Module - Assign department to employee, view employees department-wise.
(Department is already a field on each employee record; this module provides
 dedicated operations for re-assigning and viewing by department.)
"""

from utils import get_all_employees, save_all_employees, find_employee_by_id


def assign_department():
    print("\n----- Assign Department -----")
    emp_id = input("Enter Employee ID: ").strip()
    employee = find_employee_by_id(emp_id)

    if not employee:
        print("Employee not found.\n")
        return

    new_dept = input(f"Enter new Department for {employee['name']}: ").strip()

    employees = get_all_employees()
    for e in employees:
        if e["id"] == emp_id:
            e["department"] = new_dept
            break

    save_all_employees(employees)
    print("Department assigned successfully.\n")


def view_by_department():
    print("\n----- Employees by Department -----")
    employees = get_all_employees()

    if not employees:
        print("No employee records found.\n")
        return

    departments = {}
    for e in employees:
        departments.setdefault(e["department"], []).append(e)

    for dept, emp_list in departments.items():
        print(f"\nDepartment: {dept}")
        print("-" * 30)
        for e in emp_list:
            print(f"  {e['id']} - {e['name']}")
    print()
