# coding: utf-8
from .base import Base
from sqlalchemy import Column, Integer, FetchedValue, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship


class ShareHistory(Base):
    __tablename__ = 'share_history'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False, server_default=FetchedValue())
    user = relationship('User')
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('restaurant')
    share_url = Column(String(200), nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())
