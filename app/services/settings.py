from os import getenv
from importlib import import_module

# Absolute path to service package
service_name = getenv("SERVICE_NAME")
base_path = f'app.services.{service_name}'

constants = import_module(f'{base_path}.config.constants')
from app.modules.amqp_helper import AMQPHelper
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

connexion = connexion.FlaskApp(__name__, specification_dir=f'{service_name}/{constants.OPENAPI_PATH[0]}')
app = connexion.app
app.config['SQLALCHEMY_DATABASE_URI'] = constants.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
amqp = AMQPHelper()
