from os import getenv
from threading import Thread
from importlib import import_module

# Absolute path to service package
base_path = f'app.services.{getenv("SERVICE_NAME")}'

constants = import_module(f'{base_path}.config.constants')
messaging = import_module(f'{base_path}.config.messaging')
from app.config.constants import TCP_PORT
from .settings import amqp, app, connexion
from connexion.resolver import RestyResolver


def amqp_connect():
    for amqp_uri, uri_config in messaging.AMQP_CONFIG.items():
        for exchange_name, events_bindings in uri_config.items():
            amqp.connect(amqp_uri, events_bindings, exchange_name)
        # Start consuming connection queues
        Thread(target=amqp.start_consuming, args=[amqp_uri]).start()


def flask_serve():
    # Bind API operations
    connexion.add_api(constants.OPENAPI_PATH[1], resolver=RestyResolver(f'{base_path}{constants.CONTROLLER_MODULE}'))
    app.run(port=TCP_PORT)


if __name__ == '__main__':
    Thread(target=flask_serve).start()
    Thread(target=amqp_connect).start()
