from .Cart import CartViewModel
from collections import namedtuple

OrderContent = namedtuple('OrderContent', ['count', 'food', 'express_price', 'total_price'])


class OrderViewModel:
    def __init__(self, carts, theorder): #传入cart model数组和order 单个model，得到viewmodel，方便显示
        self.my_dishes = []
        self.total = 0
        self.__parse(carts, theorder)
        self.express_price = theorder.fair_price
        self.total_price = theorder.total_price

    def __parse(self, carts, theorder):
        self.my_dishes = self._map_to_order(carts,theorder)
        self.total = len(self.my_dishes)

    def _map_to_order(self, carts, theorder):
        return [CartViewModel(i)  for i in carts if i.id == theorder.cartid]



