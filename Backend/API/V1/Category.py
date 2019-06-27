# -*- coding:utf-8 -*-
from flask import jsonify

from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.FoodCategory import FoodCat
from Backend.Viewmodel.Category import CategoryViewModel

api = MyBluePrint('category')


@api.route('/<int:rid>', methods=['GET'])
@auth.login_required
def get_restaurant_category(rid):
    category = FoodCat.query.filter_by(rid=rid).all()
    list = [CategoryViewModel.category(i) for i in category]
    return jsonify(category=list, number=len(list))

