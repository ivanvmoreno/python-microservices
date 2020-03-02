from config import db
from .models.products_db.Product import Product, ProductSchema

def get_product(product_id) {
    """
    This function responds to a request for /products/{product_id}
    and returns the matching product
    :param person_id:   Product ID
    :return:            Product on success, 404 on not found
    """
    product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if product is not None:
        return ProductSchema().dump(product).data, 200
    else:
        abort(404, f'Product with ID {product_id} not found')
}

def add_product(product) {
    """
    This function responds to a request for /products/
    and creates a new product based on the received data
    :param product:   Product data for creation
    :return:          Product on success, 409 on already exists
    """
    product_id = product.get('id')

    existing_product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if existing_product is None:
        new_product = ProductSchema().load(product).data
        db.session.add(new_product)
        db.session.commit()
        return ProductSchema().dump(new_product).data, 201
    else:
        abort(409, f'A product with ID {product_id} already exists')
}

def update_product(product_id, product_data) {
    """
    This function responds to a request for /products/{product_id}
    and creates a new product based on the received data
    :param product_id:   Product to update
    :param product_data: New product data
    :return:             Updated product on success, 404 on not found
    """
    existing_product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if existing_product is not None:
        updated_product = ProductSchema().load(product_data, instance=existing_product, partial=True).data
        db.session.add(updated_product)
        db.session.commit()
        return ProductSchema().dump(updated_product).data, 204
    else:
        abort(404, f'Product with ID {product_id} not found')
}

def delete_product(product_id) {
    """
    This function responds to a request for /products/{product_id}
    and deletes the matching product
    :param product_id:   Product to update
    :return:             202 on deletion, 404 on not found
    """
    product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return 202
    else:
        abort(404, f'Product with ID {product_id} not found')
}
