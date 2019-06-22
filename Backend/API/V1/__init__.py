from flask import Blueprint
from . import Dish
from . import Comment
from . import Order
from . import Category
from . import Coupon
from . import Restaurant

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    Dish.api.register(bp_v1)
    Comment.api.register(bp_v1)
    Order.api.register(bp_v1)
    Category.api.register(bp_v1)
    Coupon.api.register(bp_v1)
    Restaurant.api.register(bp_v1)
    return bp_v1
