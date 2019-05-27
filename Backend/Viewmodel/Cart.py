from .Dish import DishViewModel
from ..Model.Dish import Dish

class CartViewModel:
    @classmethod
    def dish(cls, cart):
        return dict(
            quantity=cart.quantity,
            dish = DishViewModel(Dish.query.filter_by(id=cart.did).first()),
            pending = cart._pending
        )