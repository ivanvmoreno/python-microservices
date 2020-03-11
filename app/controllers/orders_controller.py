from ..repositories import orders_repository
from ..models.orders_db.Order import OrderSchema, OrderStatus
from ..models.orders_db.OrderProduct import OrderProductSchema, OrderProduct

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
        new_order = orders_repository.add_order(OrderSchema.load(order, partial=True).data)
        return OrderSchema().dump(new_order).data, 200
    except ValueError as error:
        return f'Error when storing order', 500

def cancel_order(order_id):
    """
    Request order cancellation
    :param order_id:    order ID
    :return:            200 on cancelled,
                        409 on order not cancellable
    """
    try:
        existing_order = orders_repository.get_order(order_id)
        if existing_order.status == OrderStatus.shipped: raise ValueError(f'Order with ID {order_id} is already shipped')
        existing_order.status = OrderStatus.cancelled
        orders_repository.update_order(existing_order)
        return f'Order with ID {order_id} cancelled', 200
    except ValueError as error:
        return f'Order with ID {order_id} cannot be cancelled', 409


def add_product_to_order(order_id, body):
    """
    Adds a product to an order
    :param order_id:    ID of order to add the product
    :param body:        schema of the product to add
    :return:            201 on success,
                        404 on order / product not found
    """
    try:
        new_order_product = orders_repository.add_product_to_order(OrderProductSchema().load(body).data)
        return 201
    except ValueError as error:
        return f'Error while adding product {product_id}', 500


def update_product_quantity(order_id, body):
    """
    Updates quantity of a product in an order
    :param order_id:    ID of order to add the product
    :param body:        (partial) schema of the product to update
    :return:            200 on success,
                        404 on order / product not found
    """
    try:
        updated_order_product = orders_repository.update_order_product(OrderProductSchema().load(body, partial=True).data)
        return OrderProductSchema().dump(updated_order_product).data, 200
    except ValueError as error:
        return f'Error while adding product {product_id}', 500


def delete_product_from_order(order_id, product_id):
    """
    Adds a product to an order
    :param order_id:        ID of order
    :param product_id:      ID of the product to remove
    :return:                201 on success,
                            404 on order / product not found
    """
    try:
        orders_repository.delete_product_from_order(order_id, product_id)
        return 202
    except ValueError as error:
        return f'Error while adding product {product_id}', 500

