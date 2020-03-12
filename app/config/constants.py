from typing import NamedTuple
from os import getenv

DB_URI = getenv('DB_URI')
AMQP_URI = getenv('AMQP_URI')
AMQP_QUEUES = {
    'customers': {
        'customers_credit_standing': 'customers_credit_standing',
        'customers_customer_exist': 'customers_customer_exist',
    },
    'notifications': {
        'notifications_email_order_approved': 'notifications_email_order_approved',
        'notifications_email_order_cancelled': 'notifications_email_order_cancelled',
    },
    'orders': {
        'orders_new_order': 'orders_new_order',
        'orders_order_created': 'orders_order_created',
        'orders_cancel_order': 'orders_cancel_order',
        'orders_order_status': 'orders_order_status',
    },
    'products': {
        'products_product_stock': 'products_product_stock',
        'products_add_order_product': 'products_add_order_product',
    },
}
EVENTS_CUSTOMERS = AMQP_QUEUES['customers']
EVENTS_NOTIFICATIONS = AMQP_QUEUES['notifications']
EVENTS_ORDERS = AMQP_QUEUES['orders']
EVENTS_PRODUCTS = AMQP_QUEUES['products']
TCP_PORT = 3000
