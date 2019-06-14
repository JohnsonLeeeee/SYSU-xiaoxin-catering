from sqlalchemy import Column, Integer, FetchedValue, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .Address import Address
from .base import Base

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True,autoincrement=True)
    host = Column(String(10),server_default=FetchedValue())
    aid = Column(Integer, ForeignKey('address.id'), nullable=False, server_default=FetchedValue())
    address = relationship('Address')
    name = Column(String(100), nullable=False, server_default=FetchedValue())
    main_image = Column(String(100), server_default=FetchedValue())
    summary = Column(String(2000), server_default=FetchedValue())
