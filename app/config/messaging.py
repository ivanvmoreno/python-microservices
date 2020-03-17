from os import getenv

# Default services exchange
AMQP_URI = getenv('AMQP_URI')
AMQP_EXCHANGE = 'test'


class ORDER_EVENTS:
    """
    Customer entity related messaging events
    """
    ORDER_CREATED = 'order-created'
    CONFIRM_ORDER = 'confirm-order'
    ORDER_CONFIRMED = 'order-confirmed'
    CANCEL_ORDER = 'cancel-order'
    ORDER_CANCELLED = 'order-cancelled'
    SHIP_ORDER = 'ship-order'
    ORDER_SHIPPED = 'order-shipped'
    CHECK_ORDER_PRODUCTS_STOCK = 'check-order-products-stock'
