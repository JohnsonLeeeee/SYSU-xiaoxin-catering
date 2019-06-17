from flask import current_app
from sqlalchemy import Column, Integer, FetchedValue, String, DateTime, Numeric, ForeignKey, Text, BigInteger
from sqlalchemy.orm import relationship
from .Coupon import Coupon
from .user import User
from .restaurant import Restaurant
from .base import Base

class Order(Base):
    __tablename__ = 'Order'

    id =  Column( Integer, primary_key=True,autoincrement=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False, server_default=FetchedValue())
    user = relationship('User')
    total_price =  Column( Numeric(10, 2), nullable=False, server_default= FetchedValue())
    fair_price =  Column( Numeric(10, 2), nullable=False, server_default= FetchedValue())
    pay_price =  Column( Numeric(10, 2), nullable=False, server_default= FetchedValue())
    # pay_sn =  Column( String(128), nullable=False, server_default= FetchedValue())
    # prepay_id =  Column( String(128), nullable=False, server_default= FetchedValue())
    note =  Column( Text, nullable=False)
    pay_time =  Column( DateTime, nullable=False, server_default= FetchedValue())
    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('Restaurant')

    @property
    def pay_status(self):
        tmp_status = self.status
        if self.status == 1:
            tmp_status = self.express_status
            if self.express_status == 1 and self.comment_status == 0:
                tmp_status = -5
            if self.express_status == 1 and self.comment_status == 1:
                tmp_status = 1
        return tmp_status

    @property
    def status_desc(self):
        return current_app.config['PAY_STATUS_DISPLAY_MAPPING'][str(self.pay_status)]


