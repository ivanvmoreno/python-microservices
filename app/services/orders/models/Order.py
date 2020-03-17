from enum import Enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


# Aliasing order status codes using an Enum
class OrderStatus(Enum):
    PENDING = 1
    CANCELLED = 2
    PAID = 3
    SHIPPED = 4
    COMPLETED = 5


class Order(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    """
    'customer_id' relationship with Customer cannot be enforced with SQLAlchemy 
    due to being stored in an independent service persistence layer
    """
    customer_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    status = db.Column(db.Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)


class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order
        sqla_session = db.session
