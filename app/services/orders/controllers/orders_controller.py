from ..settings import amqp
from app.config.messaging import AMQP_EXCHANGE
from app.config.messaging.events.orders import *
from ..models.Order import OrderSchema, OrderStatus
from ..models.OrderProduct import OrderProductSchema
from ..repositories import orders_repository


def cancel_order_cb(message):
    """
    CANCEL_ORDER event callback
    """
    try:
        body = message.body
        order_id = CancelOrderEvent.deserialize(body).order_id
        order = orders_repository.set_order_status(order_id, OrderStatus.CANCELLED)
        # ORDER_CANCELLED event dispatch
        amqp.publish(AMQP_EXCHANGE, OrderEvents.ORDER_CANCELLED, OrderCancelledEvent(order.customer_id).serialize())
    except ValueError as error:
        print('Error cancelling order', body, error)


def confirm_order_cb(message):
    """
    CONFIRM_ORDER event callback
    """
    try:
        body = message.body
        order_id = ConfirmOrderEvent.deserialize(body).order_id
        orders_repository.set_order_status(order_id, OrderStatus.PAID)
        # ORDER_CONFIRMED event dispatch
        amqp.publish(AMQP_EXCHANGE, OrderEvents.ORDER_CONFIRMED, body)
        # SHIP_ORDER event dispatch
        products = orders_repository.get_order_products(body)
        amqp.publish(AMQP_EXCHANGE, OrderEvents.SHIP_ORDER, ShipOrderEvent(products).serialize())
    except ValueError as error:
        print('Error confirming order', body, error)


def order_shipped_cb(message):
    """
    ORDER_SHIPPED event callback
    """
    try:
        body = message.body
        orders_repository.set_order_status(body, OrderStatus.SHIPPED)
    except ValueError as error:
        print('Error setting order as shipped', body, error)


def get(order_id):
    try:
        order = orders_repository.get_order(order_id)
        return OrderSchema().dump(order), 200
    except ValueError as error:
        return f'Order {order_id} not found', 404


def post(body):
    try:
        products = body.pop('products')
        order = orders_repository.add_order(OrderSchema().load(body, partial=True))
        # ORDER_CREATED event dispatch
        amqp.publish(AMQP_EXCHANGE, OrderEvents.ORDER_CREATED, OrderCreatedEvent(
            order.order_id, products, order.customer_id).serialize())
        return OrderSchema().dump(order), 200
    except ValueError as error:
        return f'Error when storing order', 500


def delete(order_id):
    try:
        existing_order = orders_repository.get_order(order_id)
        if existing_order.status == OrderStatus.shipped: raise ValueError(f'Order with ID {order_id} is already shipped')
        existing_order.status = OrderStatus.cancelled
        orders_repository.update_order(existing_order)
        return f'Order {order_id} cancelled', 204
    except ValueError as error:
        return f'Order {order_id} cannot be cancelled', 409


def add_product_to_order(order_id, body):
    try:
        orders_repository.add_product_to_order(OrderProductSchema().load(body))
        return 204
    except ValueError as error:
        return f'Error adding product to order {order_id}', 500


def update_product_quantity(order_id, body):
    try:
        updated_order_product = orders_repository.update_order_product(OrderProductSchema().load(body, partial=True))
        return OrderProductSchema().dump(updated_order_product), 200
    except ValueError as error:
        return f'Error updating product in order {order_id}', 404


def delete_product_from_order(order_id, product_id):
    try:
        orders_repository.delete_product_from_order(order_id, product_id)
        return 204
    except ValueError as error:
        return f'Error removing product from order', 500

