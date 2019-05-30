# coding: utf-8
from .base import Base
from sqlalchemy import Column, Integer, FetchedValue, ForeignKey
from sqlalchemy.orm import relationship


class ShareHistory(Base):
    __tablename__ = 'share_history'

    id = db.Column(db.Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False, server_default=FetchedValue())
    user = relationship('User')
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('restaurant')
    share_url = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
