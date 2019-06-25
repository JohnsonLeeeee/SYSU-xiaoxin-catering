# -*- coding: utf-8 -*-
from ..Model.base import db
from flask import Blueprint, jsonify
from ..libs.web_help import ops_render
from ..libs.web_help import getFormatDate
from ..Service.Statistics import StatDailySite
import datetime
route_chart = Blueprint( 'chart_page',__name__, url_prefix="/chart")


@route_chart.route("/dashboard")
def dashboard():
    now = datetime.datetime.now()
    date_before_7days = now + datetime.timedelta(days=-7)
    date_from = getFormatDate(date=date_before_7days, format="%Y-%m-%d")
    date_to = getFormatDate(date=now, format="%Y-%m-%d")

    list = StatDailySite.getdailyincome(1, date_from, date_to)

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    data = {
        "categories":[],
        "series":[
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

    # list = [["2019-6-17", 2100], ["2019-6-18", 2200], ["2019-6-19", 2000], ["2019-6-20", 1900], ["2019-6-21", 2500], ["2019-6-22", 2400]]

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    data = {
        "categories":[],
        "series":[
            {
                "name":"日营收报表",
                "data":[]
            }
        ]
    }

    if list:
        for item in list:
            data['categories'].append(item[0])
            data['series'][0]['data'].append(float(item[2]))

    resp['data'] = data
    return jsonify(resp)

