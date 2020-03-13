from os import getenv

DB_URI = getenv('DB_URI')
AMQP_URI = getenv('AMQP_URI')
EVENTS_CUSTOMERS = {
    'customers_credit_standing': 'customers_credit_standing',
    'customers_customer_exist': 'customers_customer_exist',
}
EVENTS_NOTIFICATIONS = {
    'notifications_email_order_approved': 'notifications_email_order_approved',
    'notifications_email_order_cancelled': 'notifications_email_order_cancelled',
}
EVENTS_ORDERS = {
    'orders_new_order': 'orders_new_order',
    'orders_order_created': 'orders_order_created',
    'orders_cancel_order': 'orders_cancel_order',
    'orders_order_status': 'orders_order_status',
}
EVENTS_PRODUCTS = {
    'products_product_stock': 'products_product_stock',
    'products_add_order_product': 'products_add_order_product',
}
TCP_PORT_CUSTOMERS = 8001
TCP_PORT_NOTIFICATIONS = 8002
TCP_PORT_ORDERS = 8003
TCP_PORT_PRODUCTS = 8004
