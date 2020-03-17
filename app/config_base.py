import asyncio
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .modules.amqp_helper import AMQPHelper
from .config.constants import OPENAPI_DIR


def handle_amqp_connection(amqp_uri, events_bindings, exchange_name=''):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(AMQPHelper().connect(amqp_uri, events_bindings, exchange_name))
    loop.run_forever()


connexion_app = connexion.FlaskApp(__name__, specification_dir=OPENAPI_DIR)
# FlaskApp object instance
app = connexion_app.app
db = SQLAlchemy(app)
ma = Marshmallow(app)
