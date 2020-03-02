from config import db, ma

class Order(db.Model):
    __tablename__ = "orders"
    order_id = Column(db.Integer, primary_key=True, nullable=False)
    """
    'customer_id' relationship with Customer cannot be enforced with SQLAlchemy 
    due to being stored in an independent service persistence layer
    """
    customer_id = db.Column(db.Integer, nullable=False)
    date = Column(db.DateTime,nullable=False)
    status = Column(db.String(32)(30),nullable=False)

class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order
        sqla_session = db.session
