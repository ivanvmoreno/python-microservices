from app.config.messaging import *
from ..controllers import products_controller

# AMQPHelper event bindings
AMQP_CONFIG = {
    AMQP_URI: {
        AMQP_EXCHANGE: {
            ORDER_EVENTS.CHECK_ORDER_PRODUCTS_STOCK: products_controller.check_products_cb,
            ORDER_EVENTS.SHIP_ORDER: products_controller.ship_order_cb,
        }
    }
}
