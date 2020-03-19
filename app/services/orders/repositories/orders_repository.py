from ..settings import db
from ..models.Order import Order
from ..models.OrderProduct import OrderProduct


def get_order(order_id):
    product = Order.query \
        .filter(Order.order_id == order_id) \
        .one_or_none()

    if product is not None:
        return product
    else:
        raise ValueError(f'Order {order_id} not found')


def get_order_products(order_id):
    products = OrderProduct.query \
        .filter(OrderProduct.order_id == order_id) \
        .all()

    return products


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


def set_order_status(order_id, status):
    order = get_order(order_id)
    order.status = status
    db.session.add(order)
    db.session.commit()
    return order


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

