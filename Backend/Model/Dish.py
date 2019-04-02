from sqlalchemy import Column, Integer, FetchedValue, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from Model.base import Base, db

class Dish(Base):
    __tablename__ = 'Dish'

    id =  Column( Integer, primary_key=True)
    rid = Column( Integer, ForeignKey('restaurant.id'), nullable=False, server_default= FetchedValue())
    restaurant = relationship('restaurant')
    name =  Column( String(100), nullable=False, server_default= FetchedValue())
    price =  Column( Numeric(10, 2), nullable=False, server_default= FetchedValue())
    main_image =  Column( String(100), nullable=False, server_default= FetchedValue())
    summary =  Column( String(2000), nullable=False, server_default= FetchedValue())
    stock =  Column( Integer, nullable=False, server_default= FetchedValue())
    tags =  Column( String(200), nullable=False, server_default= FetchedValue())