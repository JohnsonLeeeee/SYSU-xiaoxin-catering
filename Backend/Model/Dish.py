# -*- coding:utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import FetchedValue
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Dish(Base):
    __tablename__ = 'Dish'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=True, server_default=FetchedValue())
    restaurant = relationship('Restaurant')
    name = Column(String(100), nullable=False, server_default=FetchedValue())
    price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    main_image = Column(String(100), nullable=False, server_default=FetchedValue())
    summary = Column(String(2000), nullable=False, server_default=FetchedValue())
    stock = Column(Integer, nullable=False, server_default=FetchedValue())
    FoodCat = relationship('FoodCat')
    cid = Column(Integer, ForeignKey('FoodCat.id'), nullable=True, server_default=FetchedValue())
    tags = Column(String(200), nullable=False, server_default=FetchedValue())
