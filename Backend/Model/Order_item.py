from flask import current_app
from sqlalchemy import Column, Integer, FetchedValue, String, DateTime, Numeric, ForeignKey, Text, BigInteger
from sqlalchemy.orm import relationship

from .base import Base, db

class Order_item(Base):
    __tablename__ = 'Order_item'

    id =  Column( Integer, primary_key=True)
    oid = Column(Integer, ForeignKey('order.id'), nullable=False, server_default=FetchedValue())
    order = relationship('Order')
    quantity =  Column( Integer, nullable=False, server_default= FetchedValue())
    did = Column(Integer, ForeignKey('dish.id'), nullable=False, server_default=FetchedValue())
    dish = relationship('Dish')
