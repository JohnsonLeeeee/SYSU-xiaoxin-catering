# -*- coding:utf-8 -*-
import datetime
from sqlalchemy import func

from Backend.Model.Order import Order
from Backend.Model.Dish import Dish
from Backend.Model.Cart import Cart
from ..Model.base import db


class StatDailySite:

    # get a list of date str that is between begin_date and end_date
    @staticmethod
    def getEveryDay(begin_date, end_date):
        date_list = []
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append([date_str, 0, 0])
            begin_date += datetime.timedelta(days=1)
        return date_list

    # get a list of income info in the restaurant with restaurant_id that is between date_from and date_to
    @staticmethod
    def getdailyincome(restaurant_id, date_from, date_to):
        orderlist = db.session.query(Order).filter(Order.rid == restaurant_id,
                                                    func.date(Order.pay_time) >= datetime.datetime.strptime(date_from, "%Y-%m-%d") + datetime.timedelta(days=-1),
                                                    func.date(Order.pay_time) <= datetime.datetime.strptime(date_to, "%Y-%m-%d")).all()
        list = StatDailySite.getEveryDay(date_from, date_to)
        for order in orderlist:
            for item in list:
                if order.pay_time.strftime("%Y-%m-%d") == item[0]:
                    item[1] = item[1] + 1
                    item[2] += order.pay_price
        return list


class StatDailyFood:

    # get a list of all dishes
    @staticmethod
    def getfoodlist():
        return db.session.query(Dish).all()

    # get a list of all carts
    @staticmethod
    def getcartlist():
        return db.session.query(Cart).all()

    # get a list of food sell info in the restaurant with restaurant_id that is between date_from and date_to
    @staticmethod
    def getfooddailyinfo(restaurant_id, date_from, date_to):
        foodlist = StatDailyFood.getfoodlist()
        list = []
        for item in foodlist:
            list.append([item.id, item.name, item.price, 0, 0])
        cartlist = StatDailyFood.getcartlist()
        for cart in cartlist:
            oid = cart.orderid
            for item in list:
                if db.session.query(Order).filter(Order.id == oid).all()[0].pay_time.strftime("%Y-%m-%d") >= date_from:
                    if db.session.query(Order).filter(Order.id == oid).all()[0].pay_time.strftime("%Y-%m-%d") <= date_to:
                        if db.session.query(Order).filter(Order.id == oid).all()[0].rid == restaurant_id:
                            if cart.did == item[0]:
                                item[3] = item[3] + 1
                                item[4] += cart.quantity * cart.Dish.price

        return list
