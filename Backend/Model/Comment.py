# -*- coding:utf-8 -*-
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import FetchedValue
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Comment(Base):
    __tablename__ = 'Comment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False, server_default=FetchedValue())
    user = relationship('User')
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('Restaurant')
    content = Column(String(200), nullable=False, server_default=FetchedValue())