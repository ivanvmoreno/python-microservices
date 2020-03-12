from enum import Enum
from ...config_base import db, ma
from datetime import datetime

""" 
Aliasing order status codes using an Enum
1 - pending
2 - cancelled
3 - paid
4 - shipped
5 - completed
"""
OrderStatus = Enum('pending', 'cancelled', 'paid', 'shipped', 'completed')

class Order(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    """
    'customer_id' relationship with Customer cannot be enforced with SQLAlchemy 
    due to being stored in an independent service persistence layer
    """
    customer_id = db.db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    status = db.Column(OrderStatus, default=OrderStatus.pending, nullable=False)

class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order
        sqla_session = db.session
