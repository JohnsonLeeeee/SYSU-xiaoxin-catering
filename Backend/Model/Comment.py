from sqlalchemy import Integer, Column, String, FetchedValue, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Model.base import Base, db
from Model.user import User


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    oid = Column( Integer, ForeignKey('order.id'), nullable=False, server_default= FetchedValue())
    order = relationship('Order')
    score = Column(Integer, nullable=False, server_default=FetchedValue())
    content = Column(String(200), nullable=False, server_default=FetchedValue())
