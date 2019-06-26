import json
import datetime
from ..Model.Dish import Dish
from ..Model.Cart import Cart
from ..Model.Order import Order
from ..libs.web_help import defaultencode

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


class ItemViewModel:
    @classmethod
    def item(cls,item):
        out = dict(
            name = Dish.query.filter_by(id = item.did).first().name,
            price = Dish.query.filter_by(id = item.did).first().price,
            image = Dish.query.filter_by(id = item.did).first().main_image,
            quantity = item.quantity
        )
        return out



class OrderViewModel:
    @classmethod
    def order(cls, order):
        items = Cart.query.filter_by(orderid=order.id).all()
        list = [ItemViewModel.item(i) for i in items]
        return json.dumps(list,default=defaultencode)

    @classmethod
    def total_price(cls, order):
        out = Order.query.filter_by(id=order.id).first().total_price
        return out

    @classmethod
    def pay_price(cls, order):
        out = Order.query.filter_by(id=order.id).first().pay_price
        return out

    @classmethod
    def create_time(cls, order):
        out = Order.query.filter_by(id=order.id).first().create_time
        return json.dumps(out,default=default)