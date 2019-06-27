# -*- coding:utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import FetchedValue
from sqlalchemy import DateTime
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from .base import Base


class Order(Base):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False, server_default=FetchedValue())
    user = relationship('User')
    total_price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    pay_price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    note = Column(Text, nullable=False)
    pay_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('Restaurant')



