from ..settings import db
from ..models.Customer import Customer


def get_customer(email):
    customer = Customer.query \
        .filter(Customer.email == email) \
        .one_or_none()

    if customer is not None:
        return customer
    else:
        raise ValueError(f'Customer with {email} not found')


def get_customer_by_id(customer_id):
    customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if customer is not None:
        return customer
    else:
        raise ValueError(f'Customer with {customer_id} not found')

def add_customer(customer):
    db.session.add(customer)
    db.session.commit()
    return customer


def update_customer(customer):
    db.session.add(customer)
    db.session.commit()
    return customer


def delete_customer(email):
    customer = Customer.query \
        .filter(Customer.email == email) \
        .one_or_none()

    if customer is not None:
        db.session.delete(customer)
        db.session.commit()
        return
    else:
        raise ValueError(f'Customer {email} not found')

