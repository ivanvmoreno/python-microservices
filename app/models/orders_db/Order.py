from enum import Enum
from config import db, ma
from datetime import datetime

""" 
Aliasing order status codes using an Enum
1 - cancelled
2 - paid
3 - shipped
4 - completed
"""
order_status = Enum('cancelled', 'paid', 'shipped', 'completed')

class Order(db.Model):
    __tablename__ = "orders"
    order_id = Column(db.Integer, primary_key=True, nullable=False)
    """
    'customer_id' relationship with Customer cannot be enforced with SQLAlchemy 
    due to being stored in an independent service persistence layer
    """
    customer_id = db.Column(db.Integer, nullable=False)
    date = Column(db.DateTime, default=datetime.now(), nullable=False)
    status = Column(order_status, nullable=False)

class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order
        sqla_session = db.session
