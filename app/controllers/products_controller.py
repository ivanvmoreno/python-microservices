from ..repositories import products_repository
from ..models.products_db.Product import ProductSchema

def get_product(product_id):
    """
    Returns the matching product
    :param product_id:   product ID
    :return:            product on success, 404 on not found
    """
    try:
        product = products_repository.get_product(product_id)
        return ProductSchema().dump(product).data, 200
    except ValueError as error:
        return f'Product with ID {product_id} not found', 404


def add_product(product):
    """
    Creates a new product based on the received data
    :param product:   product data for creation
    :return:          product on success, 500 on error
    """
    try:
        new_product = products_repository.add_product(product)
        return ProductSchema().dump(new_product).data, 200
    except ValueError as error:
        return f'Error while adding product {product_id}', 500


def update_product(product_id, product_data):
    """
    Creates a new product based on the received data
    :param product_id:      ID of product to update
    :param product_data:    new product data
    :return:                updated product on success, 404 on not found
    """
    try:
        updated_product = products_repository.update_product(product_id, product_data)
        return ProductSchema().dump(updated_product).data, 200
    except ValueError as error:
        return f'Product with ID {product_id} not found', 404

def delete_product(product_id):
    """
    Deletes the matching product
    :param product_id:   product to update
    :return:             200 on deletion, 404 on not found
    """
    try:
        products_repository.delete_product(product_id)
        return f'Product with ID {order_id} deleted', 200
    except ValueError as error:
        return f'Product with ID {order_id} not found', 400

