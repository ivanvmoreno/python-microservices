from flask_sqlalchemy import SQLAlchemy
from ..models.Product import Product

db = SQLAlchemy()


def get_product(product_id):
    product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if product is not None:
        return product
    else:
        raise ValueError(f'Product with ID {product_id} not found')


def add_product(product):
    db.session.add(product)
    db.session.commit()
    return product


def update_product(product):
    db.session.add(product)
    db.session.commit()
    return product


def delete_product(product_id):
    product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return
    else:
        raise ValueError(f'Product with ID {product_id} not found')

