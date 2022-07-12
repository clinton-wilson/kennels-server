from pickle import NONE


EMPLOYEES = [
    {
        "id": 1,
        "name": "Ralph Wiggum"
    },
    {
        "id": 2,
        "name": "Stevie Nicks"
    },
    {
        "id": 3,
        "name": "Shreddy Van Halen"
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
    