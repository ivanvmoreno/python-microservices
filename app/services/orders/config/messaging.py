from app.config.messaging import *
from app.config.messaging.events.orders import *
from ..controllers import orders_controller

# AMQPHelper event bindings
AMQP_CONFIG = {
    AMQP_URI: {
        AMQP_EXCHANGE: {
            OrderEvents.CANCEL_ORDER: orders_controller.cancel_order_cb,
            OrderEvents.CONFIRM_ORDER: orders_controller.confirm_order_cb,
        }
    }
}
