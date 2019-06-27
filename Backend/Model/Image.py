# -*- coding:utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.schema import FetchedValue

from ..Model.base import Base


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_key = Column(String(60), nullable=False, server_default=FetchedValue())
