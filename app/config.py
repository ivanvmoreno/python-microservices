import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = connexion.App(__name__, specification_dir='openapi/')
db = SQLAlchemy(app)
ma = Marshmallow(app)
