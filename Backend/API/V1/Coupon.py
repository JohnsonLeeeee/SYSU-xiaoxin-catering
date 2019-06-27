# -*- coding:utf-8 -*-
from flask import jsonify

from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.Coupon import Coupon
from Backend.Viewmodel.Coupon import CouponViewModel

api = MyBluePrint('coupon')


@api.route('/<int:rid>/<int:uid>', methods=['GET'])
@auth.login_required
def get_user_coupon(rid, uid):
    coupons = Coupon.query.filter_by(uid=uid, rid=rid).all()
    coupons = [CouponViewModel.coupon(i) for i in coupons]
    return jsonify(coupons=coupons, number=len(coupons))


