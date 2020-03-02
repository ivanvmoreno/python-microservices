from config import db, ma

class Product(db.Model):
    __tablename__ = "products"
    product_id = Column(db.Integer, primary_key=True, nullable=False)
    name = Column(db.String(32), nullable=False)
    price = Column(db.Float, nullable=False)
    category = Column(db.String(32), nullable=False)
    stock_items = Column(db.Integer, nullable=False)
    reserved_items = Column(db.Integer, nullable=False)

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
        sqla_session = db.session
