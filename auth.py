"""
auth.py
Login Module - Admin login with username/password verification.
Credentials are stored in data/admin.txt as username|password
"""

from utils import read_lines, ADMIN_FILE


def login():
    """Ask for username/password and verify against admin.txt. Returns True/False."""
    print("\n===== ADMIN LOGIN =====")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for line in read_lines(ADMIN_FILE):
        parts = line.split("|")
        if len(parts) == 2 and parts[0] == username and parts[1] == password:
            print(f"\nLogin successful. Welcome, {username}!\n")
            return True

    print("\nInvalid username or password.\n")
    return False
