from typing import NamedTuple

AMQP_QUEUES: {
    customers: NamedTuple(
        'customers_credit_standing',
        'customers_customer_exist',
    ),
    notifications: NamedTuple(
        'notifications_email_order_approved',
        'notifications_email_order_cancelled',
    ),
    orders: NamedTuple(
        'orders_new_order',
        'orders_order_created',
        'orders_cancel_order',
        'orders_order_status',
    ),
    products: NamedTuple(
        'products_product_stock',
        'products_add_order_product',
    ),
}
EVENTS_CUSTOMERS = AMQP_QUEUES['customers']
EVENTS_NOTIFICATIONS = AMQP_QUEUES['notifications']
EVENTS_ORDERS = AMQP_QUEUES['orders']
EVENTS_PRODUCTS = AMQP_QUEUES['products']
TCP_PORT = 3000
