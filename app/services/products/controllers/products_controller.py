from ..repositories import products_repository
from ..models.Product import ProductSchema


async def check_products_cb(message):
    print(" [x] %r:%r" % (message.delivery.routing_key, message.body))
    await message.channel.basic_ack(message.delivery.delivery_tag)


async def ship_order_cb(message):
    print(" [x] %r:%r" % (message.delivery.routing_key, message.body))
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

