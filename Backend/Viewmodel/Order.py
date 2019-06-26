import json

from ..Model.Dish import Dish
from ..Model.Cart import Cart
from ..libs.web_help import defaultencode


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