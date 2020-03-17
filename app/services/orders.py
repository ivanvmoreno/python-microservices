from ..config_base import connexion_app, app
from ..config.constants import DB_URI, AMQP_URI, TCP_PORT_ORDERS, QUEUES_ORDERS
from connexion.resolver import RestyResolver

if __name__ == '__main__':
    connexion_app.add_api('orders.yaml', resolver=RestyResolver('app.controllers.orders_controller'))
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.run(port=TCP_PORT_ORDERS)
