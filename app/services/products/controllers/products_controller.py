from app.config.messaging import AMQP_EXCHANGE, OrderEvents
from app.modules.amqp_helper import AMQPHelper
from ..repositories import products_repository
from ..models.Product import ProductSchema


amqp = AMQPHelper()


async def check_products_cb(message):
    """
    CHECK_ORDER_PRODUCTS event callback
    """
    products = message.body.products
    try:
        for product in products:
            product_db = products_repository.get_product(product.product_id)
            # Check if can satisfy quantity for each product in the order
            if product_db.stock_items < product.quantity:
                # CANCEL_ORDER event dispatch
                amqp.publish_sync(AMQP_EXCHANGE, OrderEvents.CANCEL_ORDER, message.body.order_id)
                return
            amqp.publish_sync(AMQP_EXCHANGE, OrderEvents.CONFIRM_ORDER, message.body.order_id)
    except ValueError as error:
        print('Error checking customer billing status', message.body, error)
    finally:
        await message.channel.basic_ack(message.delivery.delivery_tag)


async def ship_order_cb(message):
    """
    SHIP_ORDER event callback
    """
    products = message.body.products
    try:
        order = orders_repository.set_order_status(order_id, OrderStatus.CANCELLED)
        # ORDER_CANCELLED event dispatch
        amqp.publish_sync(AMQP_EXCHANGE, OrderEvents.ORDER_CANCELLED, order_id)
    except ValueError as error:
        print('Error cancelling order', message.body, error)
    finally:
        await message.channel.basic_ack(message.delivery.delivery_tag)


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

