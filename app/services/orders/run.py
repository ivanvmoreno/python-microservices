from .settings import amqp, app, connexion
from .config.messaging import *
from .config.constants import TCP_PORT, OPENAPI_PATH, CONTROLLER_MODULE
from threading import Thread
from connexion.resolver import RestyResolver


def amqp_connect():
    for amqp_uri, uri_config in AMQP_CONFIG.items():
        for exchange_name, events_bindings in uri_config.items():
            amqp.connect(amqp_uri, events_bindings, exchange_name)
        # Start consuming connection queues
        Thread(target=amqp.start_consuming, args=[amqp_uri]).start()


def flask_serve():
    # Bind API operations
    connexion.add_api(OPENAPI_PATH[1], resolver=RestyResolver(CONTROLLER_MODULE))
    app.run(port=TCP_PORT)


if __name__ == '__main__':
    Thread(target=flask_serve).start()
    Thread(target=amqp_connect).start()
