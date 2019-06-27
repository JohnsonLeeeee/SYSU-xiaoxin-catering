# -*- coding:utf-8 -*-
from flask import jsonify
from datetime import datetime

from Backend.libs.exception_api import Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.Cart import Cart
from Backend.Model.Order import Order
from Backend.Form.Order import OrderForm
from Backend.Viewmodel.Order import OrderViewModel

api = MyBluePrint('order')


@api.route('/<int:rid>', methods=['PUT', 'POST'])
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
        order.note = orderinfo.note.data
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
def history_order(rid, uid):
    orders = Order.query.filter_by(rid=rid, uid=uid).all()
    list = [OrderViewModel.order(i) for i in orders]
    order_total_prices = [OrderViewModel.total_price(i) for i in orders]
    order_pay_prices = [OrderViewModel.pay_price(i) for i in orders]
    order_times = [OrderViewModel.create_time(i) for i in orders]
    return jsonify(orders=list, create_time=order_times, tota_prices=order_total_prices, pay_prices=order_pay_prices,
                   number=len(list))
