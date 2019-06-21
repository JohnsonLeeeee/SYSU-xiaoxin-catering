from .Restaurant import RestaurantService
from sqlalchemy import func
import datetime
from Backend.Model.Order import Order
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
                    item[2] += order.total_price

        return list


class StatDailyFood:

    @staticmethod
    def getfooddailyinfo(date, foodid):
        # 获取某食品每日营收等信息
        return True

class StatDailyShare:
    pass