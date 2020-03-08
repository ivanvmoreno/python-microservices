from ..config import app, amqp_ch
from connexion.resolver import RestyResolver
from ..config.constants import AMQP_QUEUES, TCP_PORT

if __name__ == '__main__':
    app.add_api('orders.yaml', resolver=RestyResolver('controllers'))
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    for queue in list(AMQP_QUEUES['orders']):
        amqp_ch.queue_declare(queue=queue)
    app.run(port=TCP_PORT)
