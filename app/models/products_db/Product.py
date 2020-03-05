from config import db, ma

class Product(db.Model):
    __tablename__ = "products"
    product_id = Column(db.Integer, primary_key=True, nullable=False)
    name = Column(db.String(32), nullable=False)
    price = Column(db.Float, nullable=False)
    category = Column(db.String(32))
    stock_items = Column(db.Integer, default=0)
    reserved_items = Column(db.Integer, default=0)

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
        sqla_session = db.session
