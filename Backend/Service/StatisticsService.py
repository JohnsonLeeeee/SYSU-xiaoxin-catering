from .Restaurant import RestaurantService
from sqlalchemy import func
import datetime
from Backend.Model.Order import Order
from Backend.Model.Dish import Dish
from Backend.Model.Cart import Cart
from Backend.Model.Share import ShareHistory
from ..Model.base import db


class StatDailySite:

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

    @staticmethod
    def getdailyincome(restaurant_id, date_from, date_to):
        # 获取每日营收
        orderlist = db.session.query(Order).filter(Order.rid == restaurant_id, Order.status==1,
                                                    func.date(Order.pay_time) >= datetime.datetime.strptime(date_from, "%Y-%m-%d"),
                                                    func.date(Order.pay_time) <= datetime.datetime.strptime(date_to, "%Y-%m-%d")).all()
        list = StatDailySite.getEveryDay(date_from, date_to)
        for order in orderlist:
            for item in list:
                if order.pay_time == item[0]:
                    item[1] = item[1] + 1
                    item[2] += order.pay_price

        return list


class StatDailyFood:

    @staticmethod
    def getfoodlist():
        return db.session.query(Dish).all()

    @staticmethod
    def getorderrid(oid):
        return db.session.query(Order.rid).filter(Order.id == oid)

    @staticmethod
    def getorderstatus(oid):
        return db.session.query(Order.status).filter(Order.id == oid)

    @staticmethod
    def getorderpaytime(oid):
        return db.session.query(Order.pay_time).filter(Order.id == oid)

    @staticmethod
    def getcartlist(restaurant_id, date_from, date_to):
        return db.session.query(Cart).filter(StatDailyFood.getorderrid(Cart.orderid) == restaurant_id, StatDailyFood.getorderstatus(Cart.orderid) == 1,
                                             func.date(StatDailyFood.getorderpaytime(Cart.orderid)) >= datetime.datetime.strptime(date_from, "%Y-%m-%d"),
                                             func.date(StatDailyFood.getorderpaytime(Cart.orderid)) <= datetime.datetime.strptime(date_to, "%Y-%m-%d")).all()

    @staticmethod
    def getfooddailyinfo(restaurant_id, date_from, date_to):
        # 获取食品每日营收等信息
        foodlist = StatDailyFood.getfoodlist()
        list = []
        for item in foodlist:
            list.append([item.id, item.name, item.price, 0, 0])
        cartlist = StatDailyFood.getcartlist(restaurant_id, date_from, date_to)
        for cart in cartlist:
            for item in list:
                if cart.did == item[0]:
                    item[3] = item[3] + 1
                    item[4] += cart.quantity * cart.Dish.price
                    break
        return list
