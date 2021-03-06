from app.config.messaging import *
from app.config.messaging.events.orders import *
from ..controllers import customers_controller

# AMQPHelper event bindings
AMQP_CONFIG = {
    AMQP_URI: {
        AMQP_EXCHANGE: {OrderEvents.ORDER_CREATED: customers_controller.order_created_cb}
    }
}
