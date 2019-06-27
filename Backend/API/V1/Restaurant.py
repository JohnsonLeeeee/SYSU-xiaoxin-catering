# -*- coding:utf-8 -*-
from flask import jsonify

from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.restaurant import Restaurant
from Backend.Viewmodel.Restaurant import RestaurantViewModel

api = MyBluePrint('restaurant')


@api.route('/<int:rid>', methods=['GET'])
@auth.login_required
def get_restaurant_info(rid):
    restaurant = Restaurant.query.filter_by(id=rid).first()
    out = RestaurantViewModel.info(restaurant)
    return jsonify(out)
