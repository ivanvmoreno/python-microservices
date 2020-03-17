from app.config.messaging import *
from ..controllers import orders_controller

# AMQPHelper event bindings
AMQP_CONFIG = {
    AMQP_URI: {
        AMQP_EXCHANGE: {
            ORDER_EVENTS.CANCEL_ORDER: orders_controller.cancel_order_cb,
            ORDER_EVENTS.CONFIRM_ORDER: orders_controller.confirm_order_cb,
        }
    }
}
