from sqlalchemy import Integer, Column, String, FetchedValue, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Model.base import Base, db
from Model.user import User


class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    uid =  Column( Integer, ForeignKey('user.id'), nullable=False, server_default= FetchedValue())
    user = relationship('User')
    did = Column( Integer, ForeignKey('dish.id'), nullable=False, server_default= FetchedValue())
    dish = relationship('Dish')
    quantity = Column(Integer, nullable=False, server_default=FetchedValue())
