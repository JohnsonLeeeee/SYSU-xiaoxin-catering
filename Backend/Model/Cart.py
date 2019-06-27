# -*- coding:utf-8 -*-
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import FetchedValue
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Cart(Base):
    __tablename__ = 'Cart'

    id = Column(Integer, primary_key=True,autoincrement=True)
    uid =  Column( Integer, ForeignKey('user.id'), nullable=False, server_default= FetchedValue())
    user = relationship('User')
    did = Column( Integer, ForeignKey('Dish.id'), nullable=False, server_default= FetchedValue())
    Dish = relationship('Dish')
    quantity = Column(Integer, nullable=False, server_default=FetchedValue())
    orderid = Column(Integer, ForeignKey('Order.id'), server_default=FetchedValue())
    Order = relationship('Order')

    def __generate_order(self, oid):
        self.orderid = oid
    # _pending = Column('pending', SmallInteger, default=1)

    # @property
    # def pending(self):
    #     return PendingStatus(self._pending)
    #
    # @pending.setter
    # def pending(self, status):
    #     self._pending = status.value


