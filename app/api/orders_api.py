from config import db
from .models.orders_db.Order import Order, OrderSchema
from .models.orders_db.OrderProduct import OrderProduct

def get_order(order_id) {
    """
    Returns the matching order
    :param order_id:    order ID
    :return:            order on success, 404 on not found
    """
    order = Order.query \
        .filter(Order.order_id == order_id) \
        .one_or_none()

    if order is not None:
        return OrderSchema().dump(order).data, 200
    else:
        abort(404, f'Order with ID {order_id} not found')
}

def add_order(order) {
    """
    Creates a new order based on the received data
    :param order:   order data for creation
    :return:        order on success, 409 on already exists
    """
    order_id = order.get('id')

    existing_order = Order.query \
        .filter(Order.order_id == order_id) \
        .one_or_none()

    if existing_order is None:
        new_order = OrderSchema().load(order).data
        db.session.add(new_order)
        db.session.commit()
        return OrderSchema().dump(new_order).data, 201
    else:
        abort(409, f'An order with ID {order_id} already exists')
}

def add_product_to_order(order_id, product_id, quantity) {
    """
    Adds a product to an existing order
    :param order_id:    order ID
    :param product_id:  product ID
    :param quantity:    product quantity
    :return:            200 on product added, 
                        404 on order / product not found, 
                        409 on product not available
    """
    order_id = order.get('id')

    existing_order = Order.query \
        .filter(Order.order_id == order_id) \
        .one_or_none()

    if existing_order is None:
        new_order = OrderSchema().load(order).data
        db.session.add(new_order)
        db.session.commit()
        return OrderSchema().dump(new_order).data, 201
    else:
        abort(409, f'An order with ID {order_id} already exists')
}

def update_order(order_id, order_data) {
    """
    Creates a new order based on the received data
    :param order_id:    order ID
    :param order_data:  new order data
    :return:            updated order on success, 404 on not found
    """
    existing_order = Order.query \
        .filter(Order.order_id == order_id) \
        .one_or_none()

    if existing_order is not None:
        updated_order = OrderSchema().load(order_data, instance=existing_order, partial=True).data
        db.session.add(updated_order)
        db.session.commit()
        return OrderSchema().dump(updated_order).data, 204
    else:
        abort(404, f'Order with ID {order_id} not found')
}

def update_order_product(order_id, product_id, new_quantity) {
    """
    Updates quantity of an order product
    :param order_id:        order ID
    :param product_id:      product ID
    :param new_quantity:    desired product quantity
    :return:                200 on updated quantity, 
                            404 on order / product not found, 
                            409 on product not available

    """
    order_product = OrderProduct.query \
        .filter(OrderProduct.order_id == order_id && OrderProduct.product_id == product_id) \
        .one_or_none()

    if order_product is not None:
        # TODO: Check for availability via products service
        order_product.update({ 'quantity': new_quantity })
        db.session.add(order_product)
        db.session.commit()
        return 200
    else:
        abort(404, f'Product with ID {product_id} not found in order {order_id}')
}

def delete_order(order_id) {
    """
    Deletes the matching order
    :param order_id:    order to update
    :return:            202 on deletion, 404 on not found
    """
    order = Order.query \
        .filter(Order.order_id == order_id) \
        .one_or_none()

    if order is not None:
        db.session.delete(order)
        db.session.commit()
        return 202
    else:
        abort(404, f'Order with ID {order_id} not found')
}

def delete_product_from_order(order_id, product_id) {
    """
    Deletes a product from an order
    :param order_id:    order ID
    :param order_id:    product ID
    :return:            202 on deletion, 404 on not found
    """
    order_product = OrderProduct.query \
        .filter(OrderProduct.order_id == order_id && OrderProduct.product_id == product_id) \
        .one_or_none()

    if order_product is not None:
        db.session.delete(order_product)
        db.session.commit()
        return 202
    else:
        abort(404, f'Product with ID {product_id} not found in order {order_id}')
}
