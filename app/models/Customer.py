from config import db, ma

class Customer(db.Model):
    __tablename__ = "customers"
    customer_id = Column(db.Integer, primary_key=True, nullable=False)
    name = Column(db.String(32), nullable=False)
    email = Column(db.String(32), nullable=False)
    phone = Column(db.Integer, nullable=False)
    billing_address = Column(db.String(32), nullable=False)
    shipping_address = Column(db.String(32), nullable=False)
    credit_standing = Column(db.Float, nullable=False)

class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer
        sqla_session = db.session