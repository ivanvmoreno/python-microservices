from app.modules.amqp_helper import AMQPHelper
from .config.constants import DB_URI, OPENAPI_PATH
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

connexion = connexion.FlaskApp(__name__, specification_dir=OPENAPI_PATH[0])
app = connexion.app
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
amqp = AMQPHelper()
