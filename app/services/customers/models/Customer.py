from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Customer(db.Model):
    __tablename__ = "customers"
    customer_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), primary_key=True)
    phone = db.Column(db.Integer)
    billing_address = db.Column(db.String(32), unique=True, nullable=False)
    shipping_address = db.Column(db.String(32), unique=True, nullable=False)
    credit_standing = db.Column(db.Float, default=0.00, nullable=False)


class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer
        sqla_session = db.session
