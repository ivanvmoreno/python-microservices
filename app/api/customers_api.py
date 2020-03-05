from config import db
from .models.customers_db.Customer import Customer, CustomerSchema

def get_customer(customer_id) {
    """
    Returns the matching customer
    :param person_id:   customer ID
    :return:            customer on success, 404 on not found
    """
    customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if customer is not None:
        return CustomerSchema().dump(customer).data, 200
    else:
        abort(404, f'Customer with ID {customer_id} not found')
}

def add_customer(customer) {
    """
    Creates a new customer based on the received data
    :param customer:    customer data for creation
    :return:            customer on success, 409 on already exists
    """
    customer_id = customer.get('id')

    existing_customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if existing_customer is None:
        new_customer = CustomerSchema().load(customer).data
        db.session.add(new_customer)
        db.session.commit()
        return CustomerSchema().dump(new_customer).data, 201
    else:
        abort(409, f'A customer with ID {customer_id} already exists')
}

def update_customer(customer_id, customer_data) {
    """
    Creates a new customer based on the received data
    :param customer_id:     ID of customer to update
    :param customer_data:   new customer data
    :return:                updated customer on success, 404 on not found
    """
    existing_customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if existing_customer is not None:
        updated_customer = CustomerSchema().load(customer_data, instance=existing_customer, partial=True).data
        db.session.add(updated_customer)
        db.session.commit()
        return CustomerSchema().dump(updated_customer).data, 204
    else:
        abort(404, f'Customer with ID {customer_id} not found')
}

def delete_customer(customer_id) {
    """
    Deletes the matching customer
    :param customer_id:     customer to update
    :return:                202 on deletion, 404 on not found
    """
    customer = Customer.query \
        .filter(Customer.customer_id == customer_id) \
        .one_or_none()

    if customer is not None:
        db.session.delete(customer)
        db.session.commit()
        return 202
    else:
        abort(404, f'Customer with ID {customer_id} not found')
}
