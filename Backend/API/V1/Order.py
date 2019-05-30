
from flask import jsonify, g

from Backend.libs.exception_api import  Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.Cart import Cart
from Backend.Model.Order import Order
from Backend.Form.Order import OrderForm

api = MyBluePrint('order')

@api.route('/', methods=['GET'])
@auth.login_required
def get_user_order():
    uid = g.user.uid
    order = Order.query.filter_by(uid=uid).all()
    return jsonify(order)


@api.route('/', methods=['PUT','POST'])
@auth.login_required
def create_order():
    uid = g.user.uid
    orderinfo = OrderForm().validate_for_api()
    with db.auto_commit():
        order = Order(uid=uid,cid=orderinfo.cid,total_price=orderinfo.total_price,fair_price=orderinfo.fair_price,
                      note=orderinfo.note,rid=orderinfo.rid,aid=orderinfo.aid)
        db.session.add(order)
        for i in orderinfo.lists.data:
            cart = Cart(uid = uid, did=i.did, quantity=i.quantity,orderid=order.id)
            db.session.add(cart)
    return Success()