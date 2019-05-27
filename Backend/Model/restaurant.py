from sqlalchemy import Column, Integer, FetchedValue, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    aid = Column(Integer, ForeignKey('address.id'), nullable=False, server_default=FetchedValue())
    address = relationship('Address')
    name = Column(String(100), nullable=False, server_default=FetchedValue())
    main_image = Column(String(100), nullable=False, server_default=FetchedValue())
    summary = Column(String(2000), nullable=False, server_default=FetchedValue())
    month_count = Column(Integer, nullable=False, server_default=FetchedValue())
    total_count = Column(Integer, nullable=False, server_default=FetchedValue())
    view_count = Column(Integer, nullable=False, server_default=FetchedValue())
    comment_count = Column(Integer, nullable=False, server_default=FetchedValue())