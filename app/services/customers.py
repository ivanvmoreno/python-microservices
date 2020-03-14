from ..config_base import connexion_app, app, amqp_ch
from ..config.constants import DB_URI, AMQP_URI, TCP_PORT_CUSTOMERS, QUEUES_CUSTOMERS
from connexion.resolver import RestyResolver

if __name__ == '__main__':
    connexion_app.add_api('customers.yaml', resolver=RestyResolver('app.controllers.customers_controller'))
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    for queue in QUEUES_CUSTOMERS:
        amqp_ch.queue_declare(queue)
    app.run(port=TCP_PORT_CUSTOMERS)
