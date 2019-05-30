from sqlalchemy import Integer, Column, String, FetchedValue, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, db
from .user import User


class Address(Base):
    __tablename__ = 'Address'

    id = Column(Integer, primary_key=True)
    uid =  Column( Integer, ForeignKey('user.id'), nullable=False, server_default= FetchedValue())
    user = relationship('user')
    province_id =  Column( Integer, nullable=False, server_default= FetchedValue())
    province_str =  Column( String(50), nullable=False, server_default= FetchedValue())
    city_id =  Column( Integer, nullable=False, server_default= FetchedValue())
    city_str =  Column( String(50), nullable=False, server_default= FetchedValue())
    area_id =  Column( Integer, nullable=False, server_default= FetchedValue())
    area_str =  Column( String(50), nullable=False, server_default= FetchedValue())
    address =  Column( String(100), nullable=False, server_default= FetchedValue())

    @property
    def content(self):
        return ' '.join([self.province_str,self.city_str,self.area_str,self.address])


