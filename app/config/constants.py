from os import getenv

# Events related to the Order entity
class ORDER_EVENTS:
    ORDER_CREATED = 'order-created'
    CONFIRM_ORDER = 'confirm-order'
    ORDER_CONFIRMED = 'order-confirmed'
    CANCEL_ORDER = 'cancel-order'
    ORDER_CANCELLED = 'order-cancelled'
    SHIP_ORDER = 'ship-order'
    ORDER_SHIPPED = 'order-shipped'
    CHECK_ORDER_PRODUCTS_STOCK = 'check-order-products-stock'


# Queues services have to listen to
QUEUES_CUSTOMERS = [ORDER_EVENTS.ORDER_CREATED]
QUEUES_ORDERS = [
    ORDER_EVENTS.CANCEL_ORDER,
    ORDER_EVENTS.CONFIRM_ORDER,
    ORDER_EVENTS.CANCEL_ORDER,
]
QUEUES_PRODUCTS = [
    ORDER_EVENTS.CHECK_ORDER_PRODUCTS_STOCK,
    ORDER_EVENTS.SHIP_ORDER,
]
QUEUES_NOTIFICATIONS = [
    ORDER_EVENTS.ORDER_CONFIRMED,
    ORDER_EVENTS.ORDER_CANCELLED,
]

# TCP ports services listen to 
TCP_PORT_CUSTOMERS = 8001
TCP_PORT_NOTIFICATIONS = 8002
TCP_PORT_ORDERS = 8003
TCP_PORT_PRODUCTS = 8004

DB_URI = getenv('DB_URI')
AMQP_URI = getenv('AMQP_URI')
