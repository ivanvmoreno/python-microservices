from ..repositories import orders_repository
from ..models.orders_db.Order import OrderSchema, OrderStatus

def get_order(order_id):
    """
    Returns the matching order
    :param order_id:    order ID
    :return:            order on success, 404 on not found
    """
    try:
        order = orders_repository.get_order(order_id)
        return OrderSchema().dump(order).data, 200
    except ValueError as error:
        return f'Order with ID {order_id} not found', 404

def add_order(order):
    """
    Creates a new order based on the received data
    :param order:   order data for creation
    :return:        order on success, 409 on already exists
    """
    try:
        new_order = orders_repository.add_order(order)
        return OrderSchema().dump(new_order).data, 200
    except ValueError as error:
        return f'An order with ID {order_id} already exists', 409

def cancel_order(order_id):
    """
    Request order cancellation
    :param order_id:    order ID
    :return:            200 on cancelled, 
                        404 on non-existing order, 
                        409 on order not cancellable
    """
    try:
        existing_order = orders_repository.get_order(order_id)
        if existing_order is None: return f'Order with ID {order_id} not found', 404
        if existing_order.status == OrderStatus.shipped: raise ValueError(f'Order with ID {order_id} is already shipped')
        orders_repository.update_order(order_id, { status: OrderStatus.cancelled })
        return f'Order with ID {order_id} cancelled', 200
    except ValueError as error:
        return f'Order with ID {order_id} cannot be cancelled', 409

