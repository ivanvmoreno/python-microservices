import asyncio
from threading import Thread
from ..modules.amqp_helper import AMQPHelper
from ..config_base import app, connexion_app, handle_amqp_connection
from ..config.constants import DB_URI, AMQP_URI, TCP_PORT_CUSTOMERS
from ..config.messaging import QUEUES_CUSTOMERS, AMQP_EXCHANGE
from connexion.resolver import RestyResolver

if __name__ == '__main__':
    connexion_app.add_api(
        'customers.yaml', 
        resolver=RestyResolver('app.controllers.customers_controller'))
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    Thread(target=handle_amqp_connection, args=[AMQP_URI, QUEUES_CUSTOMERS, AMQP_EXCHANGE]).start()
    Thread(target=app.run, kwargs={ 'port': TCP_PORT_CUSTOMERS }).start()
