CUSTOMERS = [
    {
        "id": 1,
        "name": "Carl Winslow"
    },
       {
        "id": 2,
        "name": "Davy Jones"
    },
       {
        "id": 3,
        "name": "Casey Klein"
    }
]

def get_all_customers():
    """returns all customers
    """
    return CUSTOMERS

def get_single_customer(id):
    """ returns single customer
    """
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer
    