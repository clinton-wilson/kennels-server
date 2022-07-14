import sqlite3
import json
from models import Customer, customer


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


# def get_all_customers():
#     """returns all customers
#     """
#     return CUSTOMERS

def get_all_customers():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            all_customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(all_customer.__dict__)

    return json.dumps(customers)


# def get_single_customer(id):
#     """ returns single customer
#     """
#     requested_customer = None

#     for customer in CUSTOMERS:
#         if customer["id"] == id:
#             requested_customer = customer

#     return requested_customer

def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        single_customer = Customer(data['id'], data['name'], data['address'], data['email'], data['password'])

        return json.dumps(single_customer.__dict__)

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
        