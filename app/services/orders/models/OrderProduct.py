from ..settings import db, ma


class OrderProduct(db.Model):
    __tablename__ = "order_products"
    order_id = db.Column(
        db.Integer, db.ForeignKey('Order.order_id'), primary_key=True, nullable=False
    )
    """
    'product_id' relationship with Product cannot be enforced with SQLAlchemy 
    due to being stored in an independent service persistence layer
    """
    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)


class OrderProductSchema(ma.ModelSchema):
    class Meta:
        model = OrderProduct
        sqla_session = db.session
