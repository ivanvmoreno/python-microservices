from uuid import uuid4
from ..config_base import db
from ..models.customers_db.Customer import Customer, CustomerSchema

def get_customer(customer_id):
    customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if customer is not None:
        return customer
    else:
        raise ValueError(f'Customer with ID {customer_id} not found')


def add_customer(customer):
    customer.customer_id = uuid4()
    db.session.add(customer)
    db.session.commit()
    return customer


def update_customer(customer):
    db.session.add(customer)
    db.session.commit()
    return customer


def delete_customer(customer_id):
    customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if customer is not None:
        db.session.delete(customer)
        db.session.commit()
        return
    else:
        raise ValueError(f'Customer with ID {customer_id} not found')

