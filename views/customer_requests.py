CUSTOMERS = [
    {
        "id": 1,
        "name": "Carl Winslow",
        "email": "family@matters.com"
    },
    {
        "id": 2,
        "name": "Davy Jones",
        "email": "davy@locker.com"
    },
    {
        "id": 3,
        "name": "Casey Klein",
        "email": "casey@partydown.com"
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


def delete_customer(id):
    """deletes customer"""
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """updates customers"""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
        