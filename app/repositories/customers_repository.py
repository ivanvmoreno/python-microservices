from ..config import db
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
    try:
        # TODO: generate customer ID
        db.session.add(customer)
        db.session.commit()
        return customer
    else:
        raise ValueError(f'Error while storing customer')


def update_customer(customer):
    existing_customer = Customer.query \
        .filter(Customer.customer_id == customer.customer_id) \
        .one_or_none()

    if existing_customer is not None:
        updated_customer = CustomerSchema().load(customer, instance=existing_customer, partial=True).data
        db.session.add(updated_customer)
        db.session.commit()
        return updated_customer
    else:
        raise ValueError(f'Customer with ID {customer_id} not found')


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

