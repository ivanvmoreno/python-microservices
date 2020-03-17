from flask_sqlalchemy import SQLAlchemy
from ..models.Customer import Customer

db = SQLAlchemy()


def get_customer(email):
    customer = Customer.query \
        .filter(Customer.email == email) \
        .one_or_none()

    if customer is not None:
        return customer
    else:
        raise ValueError(f'Customer with {email} not found')


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

