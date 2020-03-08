from ..config import amqp_ch
from ..repositories import customers_repository
from ..models.customers_db.Customer import CustomerSchema

def get_customer(customer_id):
    """
    Returns the matching customer
    :param person_id:   customer ID
    :return:            customer on success, 404 on not found
    """
    try:
        customer = customers_repository.get_customer(customer_id)
        return CustomerSchema().dump(customer).data, 200
    except ValueError as error:
        return f'Customer with ID {customer_id} not found', 404

def add_customer(customer):
    """
    Creates a new customer based on the received data
    :param customer:    customer data for creation
    :return:            customer on success, 500 on error
    """
    try:
        new_customer = customers_repository.add_customer(CustomerSchema().load(customer).data)
        return CustomerSchema().dump(new_customer).data, 201
    except ValueError as error:
        return f'Error while storing customer', 500
    

def update_customer(customer):
    """
    Creates a new customer based on the received data
    :param customer_data:   new customer data
    :return:                updated customer on success, 404 on not found
    """
    try:
        # TODO: update openAPI endpoint definition 
        updated_customer = customers_repository.update_customer(CustomerSchema().load(customer).data)
        return CustomerSchema().dump(updated_customer).data, 201
    except ValueError as error:
        return f'Customer with ID {customer_id} not found', 404

