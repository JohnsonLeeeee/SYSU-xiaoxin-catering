
from flask import jsonify, g

from Backend.libs.exception_api import DeleteSuccess, Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.Coupon import Coupon

api = MyBluePrint('coupon')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user_coupon():
    uid = g.user.id
    coupons = Coupon.query.filter_by(uid=uid).all()
    return jsonify(coupons)