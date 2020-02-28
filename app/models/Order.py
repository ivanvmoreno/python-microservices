from config import db, ma

class Order(db.Model):
    __tablename__ = "orders"
    orderId = Column(db.Integer, primary_key=True, nullable=False)
    date = Column(db.DateTime,nullable=False)
    status = Column(db.String(32)(30),nullable=False)

class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order
        sqla_session = db.session