# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from ..Model.base import Base


class FoodCat(Base):
    __tablename__ = 'FoodCat'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50), nullable=False, server_default=FetchedValue())
    weight = Column(Integer, nullable=False, server_default=FetchedValue()) #显示的优先级

