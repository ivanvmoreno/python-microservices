from ..config_base import db
from ..models.orders_db.Order import Order, OrderSchema
from ..models.orders_db.OrderProduct import OrderProduct

def get_order(order_id):
    product = Product.query \
        .filter(Product.product_id == product_id) \
        .one_or_none()

    if product is not None:
        return product
    else:
        raise ValueError(f'Product {product_id} not found')


def delete_order(order_id):
    order = Order.query \
        .filter(Order.order_id == order_id) \
        .one_or_none()

    if order is not None:
        db.session.delete(order)
        db.session.commit()
        return
    else:
        raise ValueError(f'Order {order_id} not found')


def add_order(order):
    db.session.add(order)
    db.session.commit()
    return order


def update_order(order):
    db.session.add(order)
    db.session.commit()
    return order


def add_product_to_order(order_product):
    db.session.add(order_product)
    db.session.commit()
    return order_product


def update_order_product(order_product):
    db.session.add(order_product)
    db.session.commit()
    return order_product


def delete_product_from_order(order_id, product_id):
    order_product = OrderProduct.query \
        .filter(OrderProduct.order_id == order_id and OrderProduct.product_id == product_id) \
        .one_or_none()

    if order_product is not None:
        db.session.delete(order_product)
        db.session.commit()
        return order_product
    else:
        raise ValueError(f'Product {product_id} not found in order {order_id}')

