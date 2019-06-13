
from flask import jsonify, g

from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.Dish import Dish

api = MyBluePrint('dish')

@api.route('/<int:rid>', methods=['GET'])
@auth.login_required
def get_restaurant_dish(rid):
    dish = Dish.query.filter_by(rid=rid).all()
    #显示具体，名称而非id
    return jsonify(dish)
