from flask import Blueprint
from . import Dish
from . import Comment
from . import Order

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    Dish.api.register(bp_v1)
    Comment.api.register(bp_v1)
    Order.api.register(bp_v1)
    # book.api.register(bp_v1)
    # client.api.register(bp_v1)
    # token.api.register(bp_v1)
    # gift.api.register(bp_v1)
    return bp_v1