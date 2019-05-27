from flask import current_app
from sqlalchemy import Column, Integer, FetchedValue, String, DateTime, Numeric, ForeignKey, Text, BigInteger
from sqlalchemy.orm import relationship

from .base import Base, db

class Order_callback(Base):
    __tablename__ = 'Order_callback'

    id =  Column( Integer, primary_key=True)
    oid = Column(Integer, ForeignKey('order.id'), nullable=False, server_default=FetchedValue())
    order = relationship('Order')
    refund_data = Column(Text, nullable=False)
