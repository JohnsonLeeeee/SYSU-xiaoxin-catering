from flask import current_app
from sqlalchemy import Column, Integer, FetchedValue, String, DateTime, Numeric, ForeignKey, Text, BigInteger
from sqlalchemy.orm import relationship

from .base import Base, db

class Coupon(Base):
    __tablename__ = 'Coupon'
    id =  Column( Integer, primary_key=True,autoincrement=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False, server_default=FetchedValue())
    user = relationship('User')
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('Restaurant')
    discount =  Column( Integer, nullable=False, server_default= FetchedValue())
    expiration_date = Column( DateTime, nullable=False, server_default= FetchedValue())
