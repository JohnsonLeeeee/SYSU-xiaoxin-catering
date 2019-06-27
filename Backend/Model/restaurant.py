# -*- coding:utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import FetchedValue
from sqlalchemy import String

from .base import Base


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, server_default=FetchedValue())
    main_image = Column(String(100), server_default=FetchedValue())
    summary = Column(String(2000), server_default=FetchedValue())
