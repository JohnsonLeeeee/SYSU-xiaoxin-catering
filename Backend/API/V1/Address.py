
from flask import jsonify, g

from Backend.libs.exception_api import  Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.Address import Address
from Backend.Form.Address import AddressForm

api = MyBluePrint('address')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user_address(uid):
    address = Address.query.filter_by(uid=uid).all()
    return jsonify(address)


@api.route('/<int:uid>', methods=['PUT','POST'])
@auth.login_required
def create_address(uid):
    uid = g.user.uid
    address_info = AddressForm().validate_for_api()
    with db.auto_commit():
        address = Address(uid=uid,province_id=address_info.province_id,city_id=address_info.city_id,
                          area_id=address_info.area_id,address=address_info.address)
        db.session.add(address)
    return Success()