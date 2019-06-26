# coding: utf-8
from sqlalchemy import func, extract
from datetime import date
import datetime
from Backend.Model.Order import Order
from Backend.Model.Comment import Comment
from ..Model.base import db

class RestaurantService:

    @staticmethod
    def get_today_order(restuarant_id):
        num = db.session.query(func.count(Order.id)).filter(Order.rid == restuarant_id, Order.status==1, func.date(Order.pay_time) == date.today() ).scalar()
        return num

    @staticmethod
    def get_month_order(restuarant_id):
        num = db.session.query(func.count(Order.id)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                            extract('month', Order.pay_time) == datetime.datetime.now().month).scalar()
        return num

    @staticmethod
    def get_month_pay(restuarant_id):
        num = db.session.query(func.sum(Order.pay_price)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                            extract('month', Order.pay_time) == datetime.datetime.now().month).scalar()
        return num

    @staticmethod
    def get_today_pay(restuarant_id):
        num = db.session.query(func.sum(Order.pay_price)).filter(Order.rid == restuarant_id, Order.status == 1,
                                                                   func.date(Order.pay_time) == date.today()).scalar()
        return num

    @staticmethod
    def get_total_pay(restuarant_id):
        num = db.session.query(func.sum(Order.pay_price)).filter(Order.rid == restuarant_id, Order.status == 1).scalar()
        return num

    @staticmethod
    def get_today_coupon(restuarant_id):
        num = db.session.query(func.count(Comment.id)).filter(Comment.rid == restuarant_id, Comment.status == 1,
                                                                   func.date(Comment.create_time) == date.today()).scalar()
        return num

    @staticmethod
    def get_month_coupon(restuarant_id):
        num = db.session.query(func.count(Comment.id)).filter(Comment.rid == restuarant_id, Comment.status == 1,
                                                             extract('month', Comment.create_time) == datetime.datetime.now().month).scalar()
        return num

