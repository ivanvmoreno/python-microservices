from ...config_base import db, ma

class Customer(db.Model):
    __tablename__ = "customers"
    customer_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32))
    phone = db.Column(db.Integer)
    billing_address = db.Column(db.String(32), nullable=False)
    shipping_address = db.Column(db.String(32), nullable=False)
    credit_standing = db.Column(db.Float, default=0.00, nullable=False)

class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer
        sqla_session = db.session