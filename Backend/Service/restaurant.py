# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, Numeric
from sqlalchemy.schema import FetchedValue
from ..libs.web_help import getCurrentDate

from sqlalchemy import func
from datetime import date
from Backend.Model.Order import Order
from Backend.Model.Share import ShareHistory
from ..Model.base import db

class RestaurantService:

    @staticmethod
    @property
    def get_today_order(restuarant_id):
        num = db.session.query(func.count(Order.id)).filter(Order.rid == restuarant_id, Order.status==1, func.date(Order.date_time) == date.today() ).all()
        return num

    @staticmethod
    @property
    def get_month_order(restuarant_id):
        num = db.session.query(func.count(Order.id)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                            func.month(Order.date_time) == date.month()).all()
        return num

    @staticmethod
    @property
    def get_month_pay(restuarant_id):
        num = db.session.query(func.sum(Order.total_price)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                            func.month(Order.date_time) == date.month()).all()
        return num

    @staticmethod
    @property
    def get_today_pay(restuarant_id):
        num = db.session.query(func.sum(Order.total_price)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                                   func.date(Order.date_time) == date.today()).all()
        return num

    @staticmethod
    @property
    def get_total_pay(restuarant_id):
        num = db.session.query(func.sum(Order.total_price)).filter(Order.rid == restuarant_id, Order.status == 1).all()
        return num

    @staticmethod
    @property
    def get_today_coupon(restuarant_id):
        num = db.session.query(func.count(Order.cid)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                                   func.date(Order.date_time) == date.today()).all()
        return num

    @staticmethod
    @property
    def get_month_coupon(restuarant_id):
        num = db.session.query(func.count(Order.cid)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                             func.month(Order.date_time) == date.month()).all()
        return num

    @staticmethod
    @property
    def get_today_share(restuarant_id):
        num = db.session.query(func.count(ShareHistory.id)).filter(ShareHistory.rid == restuarant_id, ShareHistory.status == 1,
                                                             func.date(ShareHistory.created_time) == date.today()).all()
        return num

    @staticmethod
    @property
    def get_month_share(restuarant_id):
        num = db.session.query(func.count(ShareHistory.id)).filter(ShareHistory.rid == restuarant_id,
                                                                   ShareHistory.status == 1,
                                                                   func.month(ShareHistory.created_time) == date.month()).all()
        return num

class StatDailySite(db.Model):
    __tablename__ = 'stat_daily_site'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True)
    total_pay_money = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue())
    total_member_count = db.Column(db.Integer, nullable=False)
    total_new_member_count = db.Column(db.Integer, nullable=False)
    total_order_count = db.Column(db.Integer, nullable=False)
    total_shared_count = db.Column(db.Integer, nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
