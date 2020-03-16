from .modules.amqp_helper import AMQPHelper
import asyncio, connexion, time
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

def handle_amqp_connection(amqp_uri, events_bindings, exchange_name = ''):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(AMQPHelper().connect(amqp_uri, events_bindings, exchange_name))
    loop.run_forever()

connexion_app = connexion.FlaskApp(__name__, specification_dir='openapi/')
# FlaskApp object instance
app = connexion_app.app
db = SQLAlchemy(app)
ma = Marshmallow(app)
