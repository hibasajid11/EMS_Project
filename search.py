"""
search.py
Search Module - Search employee by ID, Name, or Department.
"""

from utils import get_all_employees


def _print_results(results):
    if not results:
        print("No matching employee found.\n")
        return

    print(f"{'ID':<8}{'Name':<15}{'Department':<15}{'Salary':<10}{'Bonus%':<8}")
    print("-" * 56)
    for e in results:
        print(f"{e['id']:<8}{e['name']:<15}{e['department']:<15}{e['salary']:<10}{e['bonus']:<8}")
    print()


def search_by_id():
    print("\n----- Search by ID -----")
    emp_id = input("Enter Employee ID: ").strip()
    results = [e for e in get_all_employees() if e["id"] == emp_id]
    _print_results(results)


def search_by_name():
    print("\n----- Search by Name -----")
    name = input("Enter Name (or part of name): ").strip().lower()
    results = [e for e in get_all_employees() if name in e["name"].lower()]
    _print_results(results)


def search_by_department():
    print("\n----- Search by Department -----")
    dept = input("Enter Department: ").strip().lower()
    results = [e for e in get_all_employees() if dept in e["department"].lower()]
    _print_results(results)
