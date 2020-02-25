from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    orderId = Column(
        Integer, 
        primary_key=True, 
        nullable=False
    )
    date = Column(
        DateTime,
        nullable=False
    )
    status = Column(
        String(30),
        nullable=False    
    )


class Customer(Base):
    __tablename__ = "customers"

    customerId = Column(
        Integer, 
        primary_key=True, 
        nullable=False
    )
    name = Column(
        String,
        nullable=False
    )
    email = Column(
        String,
        nullable=False
    )
    phone = Column(
        Integer,
        nullable=False
    )
    billingAddress = Column(
        String,
        nullable=False
    )
    shippingAddress = Column(
        String,
        nullable=False
    )
    creditStanding = Column(
        Float,
        nullable=False
    )


class Product(Base):
    __tablename__ = "products"

    productId = Column(
        Integer, 
        primary_key=True, 
        nullable=False
    )
    name = Column(
        String,
        nullable=False
    )
    price = Column(
        Float,
        nullable=False
    )
    category = Column(
        String,
        nullable=False
    )
    stockItems = Column(
        Integer,
        nullable=False
    )
    reservedItems = Column(
        Integer, 
        nullable=False
    )

