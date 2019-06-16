
from flask import jsonify, g

from Backend.libs.exception_api import DeleteSuccess, Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.Coupon import Coupon
from Backend.Viewmodel.Coupon import CouponViewModel

api = MyBluePrint('coupon')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user_coupon():
    uid = g.user.id
    coupons = Coupon.query.filter_by(uid=uid).all()
    coupons = [CouponViewModel.coupon(i) for i in coupons]
    return jsonify(coupons = coupons,number = len(coupons))