# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.ext.login import login_required
from flask_login import current_user

from ..Model.administrator import Adminstrator
from ..libs.web_help import ops_render
from ..Service.Restaurant import RestaurantService

route_index = Blueprint('index', __name__, url_prefix='/')


@route_index.route("/")
@login_required
def index():
    resp_data = {
        'data':{
            'finance': {
                'total': 0,
                'today': 0,
                'month': 0
            },
            'coupon': {
                'month_new': 0,
                'total': 0
            },
            'order': {
                'today': 0,
                'month': 0
            },
            'shared': {
                'today': 0,
                'month': 0
            },
        }
    }

    data = resp_data['data']
    rid = Adminstrator.query.filter_by(id=current_user.id).first().rid
    data['finance']['month'] = RestaurantService.get_month_pay(rid)
    data['coupon']['month_new'] = RestaurantService.get_month_coupon(rid)
    data['finance']['total'] = RestaurantService.get_today_pay(rid)
    data['order']['month'] = RestaurantService.get_month_order(rid)
    data['finance']['today'] = RestaurantService.get_today_pay(rid)
    data['coupon']['today_new'] = RestaurantService.get_today_coupon(rid)
    data['order']['today'] = RestaurantService.get_today_order(rid)

    return ops_render("index/index.html", resp_data)