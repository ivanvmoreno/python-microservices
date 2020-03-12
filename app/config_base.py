import connexion, pika
from .config.constants import AMQP_URI
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

connexion_app = connexion.FlaskApp(__name__, specification_dir='openapi/')
# FlaskApp object instance
app = connexion_app.app
db = SQLAlchemy(app)
ma = Marshmallow(app)
amqp_conn = pika.BlockingConnection(pika.URLParameters(AMQP_URI))
amqp_ch = amqp_conn.channel()
