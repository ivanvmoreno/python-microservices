from ..repositories import orders_repository
from ..models.Order import OrderSchema, OrderStatus
from ..models.OrderProduct import OrderProductSchema


async def cancel_order_cb(message):
    print(" [x] %r:%r" % (message.delivery.routing_key, message.body))
    await message.channel.basic_ack(message.delivery.delivery_tag)


async def confirm_order_cb(message):
    print(" [x] %r:%r" % (message.delivery.routing_key, message.body))
    await message.channel.basic_ack(message.delivery.delivery_tag)


def get(order_id):
    try:
        order = orders_repository.get_order(order_id)
        return OrderSchema().dump(order), 200
    except ValueError as error:
        return f'Order {order_id} not found', 404


def post(order):
    try:
        # Remove 'products' key, as it's not part of the Order entity, but of the OrderProduct relation
        # Send event products
        # Send event customer
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
        new_order_product = orders_repository.add_product_to_order(OrderProductSchema().load(body))
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

