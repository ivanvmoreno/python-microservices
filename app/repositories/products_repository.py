from ..config import db
from ..models.products_db.Product import Product, ProductSchema

def get_product(product_id):
    product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if product is not None:
        return product
    else:
        raise ValueError(f'Product with ID {product_id} not found')


def add_product(product):
    # TODO: generate product ID

    existing_product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if existing_product is None:
        new_product = ProductSchema().load(product).data
        db.session.add(new_product)
        db.session.commit()
        return ProductSchema().dump(new_product).data, 201
    else:
        raise ValueError(f'Error while adding product {product_id}')


def update_product(product_id, product_data):
    existing_product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if existing_product is not None:
        updated_product = ProductSchema().load(product_data, instance=existing_product, partial=True).data
        db.session.add(updated_product)
        db.session.commit()
        return updated_product
    else:
        raise ValueError(f'Product with ID {product_id} not found')


def delete_product(product_id):
    product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return 202
    else:
        abort(404, f'Product with ID {product_id} not found')
