from ..settings import amqp
from app.config.messaging import AMQP_EXCHANGE
from app.config.messaging.events.orders import *
from ..repositories import products_repository
from ..models.Product import ProductSchema


def check_products_cb(message):
    """
    CHECK_ORDER_PRODUCTS event callback
    """
    try:
        body = message.body
        event = CheckOrderProducts.deserialize(body)
        for product in event.products:
            product_quantity = product.get('quantity')
            product_db = products_repository.get_product(product.get('product_id'))
            # Check if can satisfy quantity for each product in the order
            if product_db.stock_items < product_quantity:
                # CANCEL_ORDER event dispatch
                amqp.publish_sync(AMQP_EXCHANGE, OrderEvents.CANCEL_ORDER, event.order_id)
                return
            # Update product reserved stock
            product_db.reserved_items -= product_quantity
            products_repository.update_product(product_db)
            # CANCEL_ORDER event dispatch
            amqp.publish(AMQP_EXCHANGE, OrderEvents.CONFIRM_ORDER, event.order_id)
    except ValueError as error:
        print('Error checking customer billing status', body, error)


def ship_order_cb(message):
    """
    SHIP_ORDER event callback
    """
    try:
        body = message.body
        event = ShipOrderEvent.deserialize(body)
        for product in event.products:
            # Update product stock
            product_db = products_repository.get_product(product.product_id)
            quantity = product.get('quantity')
            product_db.stock_items -= quantity
            product_db.reserved_items += quantity
            products_repository.update_product(product_db)
            # ORDER_SHIPPED event dispatch
            amqp.publish(AMQP_EXCHANGE, OrderEvents.ORDER_SHIPPED, OrderShippedEvent(event.order_id).serialize())
    except ValueError as error:
        print('Error checking customer billing status', body, error)


def get(product_id):
    try:
        product = products_repository.get_product(product_id)
        return ProductSchema().dump(product), 200
    except ValueError as error:
        return f'Product with ID {product_id} not found', 404


def post(body):
    try:
        new_product = products_repository.add_product(ProductSchema().load(body, partial=True))
        return ProductSchema().dump(new_product), 200
    except ValueError as error:
        return f'Error creating product', 500


def put(body):
    try:
        updated_product = products_repository.update_product(ProductSchema().load(body, partial=True))
        return ProductSchema().dump(updated_product), 202
    except ValueError as error:
        return f'Product not found', 404


def delete(product_id):
    try:
        products_repository.delete_product(product_id)
        return f'Product with ID {product_id} deleted', 204
    except ValueError as error:
        return f'Product not found', 400

