from config import db, ma

class Product(db.Model):
    __tablename__ = "products"
    productId = Column(db.Integer, primary_key=True, nullable=False)
    name = Column(db.String(32), nullable=False)
    price = Column(db.Float, nullable=False)
    category = Column(db.String(32), nullable=False)
    stockItems = Column(db.Integer, nullable=False)
    reservedItems = Column(db.Integer, nullable=False)

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
        sqla_session = db.session
