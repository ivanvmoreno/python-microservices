from .constants import AMQP_URI
from ..controllers import customers_controller
# from ..controllers import customers_controller, orders_controller, products_controller

AMQP_EXCHANGE = 'test'

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

# Events services have to listen to and their associated callbacks
AMQP_CUSTOMERS = {
    AMQP_URI: {
        AMQP_EXCHANGE: {ORDER_EVENTS.ORDER_CREATED: customers_controller.order_created_cb}
    }
}
# QUEUES_ORDERS = {
#     ORDER_EVENTS.CANCEL_ORDER: orders_controller.cancel_order_cb,
#     ORDER_EVENTS.CONFIRM_ORDER: orders_controller.confirm_order_cb,
#     ORDER_EVENTS.CANCEL_ORDER: orders_controller.cancel_order_cb,
# }
# QUEUES_PRODUCTS = {
#     ORDER_EVENTS.CHECK_ORDER_PRODUCTS_STOCK: products_controller.check_products_cb,
#     ORDER_EVENTS.SHIP_ORDER: products_controller.ship_order_cb,
# }
# QUEUES_NOTIFICATIONS = [
#     ORDER_EVENTS.ORDER_CONFIRMED,
#     ORDER_EVENTS.ORDER_CANCELLED,
# ]
