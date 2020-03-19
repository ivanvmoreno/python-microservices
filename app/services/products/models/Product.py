from ..settings import db, ma

class Product(db.Model):
    __tablename__ = "products"
    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(32))
    stock_items = db.Column(db.Integer, default=0, nullable=False)
    reserved_items = db.Column(db.Integer, default=0, nullable=False)


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
        sqla_session = db.session
