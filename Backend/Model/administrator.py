from sqlalchemy import Column, Integer, ForeignKey, FetchedValue
from sqlalchemy.orm import relationship

from .user import  User

class Adminstrator(User):
    __tablename__ = 'Adminstrator'

    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('restaurant')

