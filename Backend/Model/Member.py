from sqlalchemy import Column, Integer, ForeignKey, FetchedValue
from sqlalchemy.orm import relationship

from Model.user import  User

class Member(User):
    __tablename__ = 'member'

    address = relationship('Address')
    aid = Column(Integer, ForeignKey('address.id'), nullable=False, server_default=FetchedValue())

