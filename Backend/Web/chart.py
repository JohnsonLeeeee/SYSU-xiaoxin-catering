# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import jsonify
import datetime

from ..libs.web_help import getFormatDate
from ..Service.Statistics import StatDailySite

route_chart = Blueprint('chart_page', __name__, url_prefix="/chart")


@route_chart.route("/dashboard")
def dashboard():
    now = datetime.datetime.now()
    date_before_7days = now + datetime.timedelta(days=-7)
    date_from = getFormatDate(date=date_before_7days, format="%Y-%m-%d")
    date_to = getFormatDate(date=now, format="%Y-%m-%d")

    list = StatDailySite.getdailyincome(1, date_from, date_to)

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    data = {
        "categories": [],
        "series": [
            {
                "name": "订单总数",
                "data": []
            }
        ]
    }

    if list:
        for item in list:
            data['categories'].append(item[0])
            data['series'][0]['data'].append(item[1])

    resp['data'] = data
    return jsonify(resp)


@route_chart.route("/finance")
def finance():
    now = datetime.datetime.now()
    date_before_7days = now + datetime.timedelta(days=-7)
    date_from = getFormatDate(date=date_before_7days, format="%Y-%m-%d")
    date_to = getFormatDate(date=now, format="%Y-%m-%d")

    list = StatDailySite.getdailyincome(1, date_from, date_to)

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    data = {
        "categories": [],
        "series":[
            {
                "name": "日营收报表",
                "data": []
            }
        ]
    }

    if list:
        for item in list:
            data['categories'].append(item[0])
            data['series'][0]['data'].append(float(item[2]))

    resp['data'] = data
    return jsonify(resp)

