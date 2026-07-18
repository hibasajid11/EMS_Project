"""
main.py
Entry point for the Employee Management System.
Run this file: python main.py
"""

from utils import ensure_data_files
from auth import login
from employee import add_employee, view_employees, update_employee, delete_employee
from department import assign_department, view_by_department
from salary import set_salary, calculate_net_salary
from attendance import mark_attendance, view_attendance, count_attendance
from search import search_by_id, search_by_name, search_by_department
from report import generate_report


def employee_menu():
    while True:
        print("""
----- Employee Management -----
1. Add Employee
2. View Employees
3. Update Employee
4. Delete Employee
0. Back to Main Menu
""")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "0":
            break
        else:
            print("Invalid choice.\n")


def department_menu():
    while True:
        print("""
----- Department -----
1. Assign Department
2. View Employees Department-wise
0. Back to Main Menu
""")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            assign_department()
        elif choice == "2":
            view_by_department()
        elif choice == "0":
            break
        else:
            print("Invalid choice.\n")


def salary_menu():
    while True:
        print("""
----- Salary Management -----
1. Set Salary / Bonus
2. Calculate Net Salary
0. Back to Main Menu
""")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            set_salary()
        elif choice == "2":
            calculate_net_salary()
        elif choice == "0":
            break
        else:
            print("Invalid choice.\n")


def attendance_menu():
    while True:
        print("""
----- Attendance -----
1. Mark Attendance
2. View Attendance Record
3. Count Present/Absent Days
0. Back to Main Menu
""")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            count_attendance()
        elif choice == "0":
            break
        else:
            print("Invalid choice.\n")


def search_menu():
    while True:
        print("""
----- Search -----
1. Search by ID
2. Search by Name
3. Search by Department
0. Back to Main Menu
""")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            search_by_id()
        elif choice == "2":
            search_by_name()
        elif choice == "3":
            search_by_department()
        elif choice == "0":
            break
        else:
            print("Invalid choice.\n")


def main_menu():
    while True:
        print("""
========================================
   EMPLOYEE MANAGEMENT SYSTEM - MAIN MENU
========================================
1. Employee Management
2. Department
3. Salary Management
4. Attendance
5. Search
6. Report
0. Logout / Exit
""")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            employee_menu()
        elif choice == "2":
            department_menu()
        elif choice == "3":
            salary_menu()
        elif choice == "4":
            attendance_menu()
        elif choice == "5":
            search_menu()
        elif choice == "6":
            generate_report()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


def run():
    ensure_data_files()
    print("====================================")
    print(" WELCOME TO EMPLOYEE MANAGEMENT SYSTEM")
    print("====================================")

    if login():
        main_menu()
    else:
        print("Exiting program.")


if __name__ == "__main__":
    run()
