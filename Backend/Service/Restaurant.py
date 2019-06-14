# coding: utf-8
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
        return len(num)

    @staticmethod
    @property
    def get_month_order(restuarant_id):
        num = db.session.query(func.count(Order.id)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                            func.month(Order.date_time) == date.month()).all()
        return len(num)

    @staticmethod
    @property
    def get_month_pay(restuarant_id):
        num = db.session.query(func.sum(Order.total_price)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                            func.month(Order.date_time) == date.month()).all()
        return len(num)

    @staticmethod
    @property
    def get_today_pay(restuarant_id):
        num = db.session.query(func.sum(Order.total_price)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                                   func.date(Order.date_time) == date.today()).all()
        return len(num)

    @staticmethod
    @property
    def get_total_pay(restuarant_id):
        num = db.session.query(func.sum(Order.total_price)).filter(Order.rid == restuarant_id, Order.status == 1).all()
        return len(num)

    @staticmethod
    @property
    def get_today_coupon(restuarant_id):
        num = db.session.query(func.count(Order.cid)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                                   func.date(Order.date_time) == date.today()).all()
        return len(num)

    @staticmethod
    @property
    def get_month_coupon(restuarant_id):
        num = db.session.query(func.count(Order.cid)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                             func.month(Order.date_time) == date.month()).all()
        return len(num)

    @staticmethod
    @property
    def get_today_share(restuarant_id):
        num = db.session.query(func.count(ShareHistory.id)).filter(ShareHistory.rid == restuarant_id, ShareHistory.status == 1,
                                                             func.date(ShareHistory.created_time) == date.today()).all()
        return len(num)

    @staticmethod
    @property
    def get_month_share(restuarant_id):
        num = db.session.query(func.count(ShareHistory.id)).filter(ShareHistory.rid == restuarant_id,
                                                                   ShareHistory.status == 1,
                                                                   func.month(ShareHistory.created_time) == date.month()).all()
        return len(num)
