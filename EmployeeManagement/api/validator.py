import re

def check_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(pattern, email):
        return True
    return False

def check_contact(phone_number):
    pattern = r"^\+?[0-9\s.\-\(\)]{6,18}[0-9]$"
    if re.fullmatch(pattern, phone_number):
        return True
    return False

def check_salary(salary):
    if float(salary) > 0:
        return True
    return False