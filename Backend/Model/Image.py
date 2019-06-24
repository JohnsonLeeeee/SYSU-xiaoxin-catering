from ..Model.base import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue

class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True,autoincrement=True)
    file_key = Column(String(60), nullable=False, server_default=FetchedValue())
