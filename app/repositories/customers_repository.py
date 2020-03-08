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
    # TODO: generate customer ID

    existing_customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if existing_customer is None:
        new_customer = CustomerSchema().load(customer).data
        db.session.add(new_customer)
        db.session.commit()
        return new_customer
    else:
        raise ValueError(f'A customer with ID {customer_id} already exists')


def update_customer(customer_id, customer_data):
    existing_customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if existing_customer is not None:
        updated_customer = CustomerSchema().load(customer_data, instance=existing_customer, partial=True).data
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

