
from flask import jsonify, g

from Backend.libs.exception_api import DeleteSuccess, Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.Coupon import Coupon
from Backend.Form.Cart import CartForm

api = MyBluePrint('cart')

@api.route('/<int:uid>/coupon', methods=['GET'])
@auth.login_required
def get_user_coupon():
    uid = g.user.id
    coupons = Coupon.query.filter_by(uid=uid).all()
    res = [get_coupon(i.id) for i in coupons]
    return jsonify(res)

def get_coupon(couponid):
    coupon = Coupon.query.filter_by(id=couponid).first_or_404()
    return coupon
