from pickle import NONE


EMPLOYEES = [
    {
        "id": 1,
        "name": "Ralph Wiggum",
        "address": "123 Springfield St",
        "locationId": 3
    },
    {
        "id": 2,
        "name": "Stevie Nicks",
        "address": "450 Roumour Way",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Shreddy Van Halen",
        "address": "100 Guitar St",
        "locationId": 4
    }
]

def get_all_employees():
    """returns all employees
    """
    return EMPLOYEES

def get_single_employee(id):
    """returns single employee
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    """creates new employee"""
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id

    employee['id'] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    """deletes employee"""

    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """updates employee"""
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
