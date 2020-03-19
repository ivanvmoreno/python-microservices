from ...settings import amqp
from app.config.messaging import AMQP_EXCHANGE
from app.config.messaging.events.orders import *
from ..repositories import customers_repository
from ..models.Customer import CustomerSchema


def order_created_cb(message):
    """
    ORDER_CREATED event callback
    """
    try:
        body = message.body
        event = OrderCreatedEvent.deserialize(body)
        customer = customers_repository.get_customer_by_id(event.customer_id)
        # Check if unpaid previous invoices
        if customer.credit_standing > 0:
            # CHECK_ORDER_PRODUCTS_STOCK event dispatch
            amqp.publish(
                AMQP_EXCHANGE, OrderEvents.CHECK_ORDER_PRODUCTS_STOCK, CheckOrderProducts(event.products, event.order_id).serialize())
        else:
            # CANCEL_ORDER event dispatch
            amqp.publish(AMQP_EXCHANGE, OrderEvents.CANCEL_ORDER, CancelOrderEvent(event.order_id).serialize())
    except ValueError as error:
        print('Error checking customer billing status', body, error)


def get(email):
    try:
        customer = customers_repository.get_customer(email)
        return CustomerSchema().dump(customer), 200
    except ValueError as error:
        return f'Customer {email} not found', 404


def post(body):
    try:
        new_customer = customers_repository.add_customer(CustomerSchema().load(body, partial=True))
        return CustomerSchema().dump(new_customer), 201
    except ValueError as error:
        return f'Error creating customer', 500
    

def put(body):
    try:
        updated_customer = customers_repository.update_customer(CustomerSchema().load(body, partial=True))
        return CustomerSchema().dump(updated_customer), 200
    except ValueError as error:
        return f'Customer not found', 404


def delete(email):
    try:
        customers_repository.delete_customer(email)
        return 204
    except ValueError as error:
        return f'Customer {email} not found', 404

