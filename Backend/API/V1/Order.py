
from flask import jsonify, g

from Backend.libs.exception_api import DeleteSuccess, Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.Cart import Cart
from Backend.Form.Cart import CartForm

api = MyBluePrint('order')

@api.route('/<int:oid>', methods=['GET'])
@auth.login_required
def get_order(cid):
    with db.auto_commit():
        cart = Cart.query.filter_by(id=cid).first_or_404()
        cart.delete()
    return DeleteSuccess()


@api.route('/cart', methods=['PUT','POST'])
@auth.login_required
def create_cart():
    uid = g.user.uid
    cartinfo = CartForm().validate_for_api()
    with db.auto_commit():
        for i in cartinfo.lists.data:
            cart = Cart(uid = uid, did=i.did, quantity=i.quantity)
            db.session.add(cart)
    return Success()