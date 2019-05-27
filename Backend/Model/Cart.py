from sqlalchemy import Integer, Column, SmallInteger, FetchedValue, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, db


class Cart(Base):
    __tablename__ = 'Cart'

    id = Column(Integer, primary_key=True)
    uid =  Column( Integer, ForeignKey('user.id'), nullable=False, server_default= FetchedValue())
    user = relationship('User')
    did = Column( Integer, ForeignKey('dish.id'), nullable=False, server_default= FetchedValue())
    dish = relationship('Dish')
    quantity = Column(Integer, nullable=False, server_default=FetchedValue())
    _pending = Column('pending', SmallInteger, default=1)

    # @property
    # def pending(self):
    #     return PendingStatus(self._pending)
    #
    # @pending.setter
    # def pending(self, status):
    #     self._pending = status.value


