# -*- coding:utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import FetchedValue
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Coupon(Base):
    __tablename__ = 'Coupon'
    id =  Column( Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False, server_default=FetchedValue())
    user = relationship('User')
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('Restaurant')
    discount =  Column( Integer, nullable=False, server_default= FetchedValue())
    expiration_date = Column( DateTime, nullable=False, server_default= FetchedValue())
