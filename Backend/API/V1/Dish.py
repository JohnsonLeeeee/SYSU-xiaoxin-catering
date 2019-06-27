# -*- coding:utf-8 -*-
from flask import jsonify

from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.Dish import Dish
from Backend.Viewmodel.Dish import DishViewModel

api = MyBluePrint('dish')


@api.route('/<int:rid>', methods=['GET'])
@auth.login_required
def get_restaurant_dish(rid):
    dishes = Dish.query.filter_by(rid=rid).all()
    list = [DishViewModel.dishlist(i) for i in dishes]
    return jsonify(dishes=list, number=len(list))


@api.route('/<int:rid>/<int:did>', methods=['GET'])
@auth.login_required
def get_restaurant_dish_detail(rid, did):
    dish = Dish.query.filter_by(rid=rid, id=did).first()
    dish = DishViewModel.detail(dish)
    return jsonify(dish)
