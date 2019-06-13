from sqlalchemy import Integer, Column, String, FetchedValue, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, db


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False, server_default=FetchedValue())
    user = relationship('User')
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('Restaurant')
    content = Column(String(200), nullable=False, server_default=FetchedValue())
