import connexion, pika
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = connexion.App(__name__, specification_dir='openapi/')
db = SQLAlchemy(app)
ma = Marshmallow(app)
amqp_conn = pika.BlockingConnection(pika.URLParameters(''))
amqp_ch = amqp_connection.channel()
