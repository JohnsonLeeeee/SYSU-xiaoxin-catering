
from flask import jsonify, g

from Backend.libs.exception_api import  Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.Cart import Cart
from Backend.Model.Order import Order
from Backend.Form.Order import OrderForm
from Backend.Viewmodel.Order import OrderViewModel
from datetime import datetime

api = MyBluePrint('order')

@api.route('/<int:rid>', methods=['PUT','POST'])
@auth.login_required
def create_order(rid):
    orderinfo = OrderForm().validate_for_api()
    with db.auto_commit():
        uid = orderinfo.uid.data
        order = Order()
        order.uid = uid
        order.total_price = orderinfo.total_price.data
        order.coupon_discount = orderinfo.coupon_discount.data
        pay_price = orderinfo.total_price.data - orderinfo.coupon_discount.data
        order.pay_price = pay_price
        order.pay_time = datetime.now()
        order.note=orderinfo.note.data
        order.rid = rid
        db.session.add(order)

    with db.auto_commit():
        for i in orderinfo.lists.data:
            cart = Cart()
            cart.uid = uid
            cart.did = i['did']
            cart.quantity = i['quantity']
            cart.orderid = order.id
            db.session.add(cart)
    return Success()

@api.route('/<int:rid>/<int:uid>', methods=['GET'])
@auth.login_required
def history_order(rid,uid):
    orders = Order.query.filter_by(rid=rid,uid=uid).all()
    list = [OrderViewModel.order(i) for i in orders]
    return jsonify(orders = list, number = len(list))