# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
import datetime

from ..libs.web_help import ops_render
from ..libs.web_help import getFormatDate
from ..libs.web_help import iPagination
from ..Service.Statistics import StatDailySite
from ..Service.Statistics import StatDailyFood
from ..Config.settings import PAGE_DISPLAY
from ..Config.settings import PAGE_SIZE

route_stat = Blueprint('stat', __name__, url_prefix="/stat")


@route_stat.route("/index")
def index():
    now = datetime.datetime.now()
    date_before_7days = now + datetime.timedelta(days=-7)
    default_date_from = getFormatDate(date=date_before_7days, format="%Y-%m-%d")
    default_date_to = getFormatDate(date=now, format="%Y-%m-%d")

    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    date_from = req['date_from'] if 'date_from' in req else default_date_from
    date_to = req['date_to'] if 'date_to' in req else default_date_to
    query = StatDailySite.getdailyincome(1, date_from, date_to)

    page_params = {
        'total': len(query),
        'page_size': PAGE_SIZE,
        'page': page,
        'display': PAGE_DISPLAY,
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)

    list = query
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['current'] = 'index'
    resp_data['search_con'] = {
        'date_from': date_from,
        'date_to': date_to
    }
    return ops_render("stat/index.html", resp_data)


@route_stat.route("/food")
def food():
    now = datetime.datetime.now()
    date_before_7days = now + datetime.timedelta(days=-7)
    default_date_from = getFormatDate(date=date_before_7days, format="%Y-%m-%d")
    default_date_to = getFormatDate(date=now, format="%Y-%m-%d")

    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    date_from = req['date_from'] if 'date_from' in req else default_date_from
    date_to = req['date_to'] if 'date_to' in req else default_date_to
    query = StatDailyFood.getfooddailyinfo(1, date_from, date_to)

    page_params = {
        'total': len(query),
        'page_size': PAGE_SIZE,
        'page': page,
        'display': PAGE_DISPLAY,
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)

    resp_data['list'] = query
    resp_data['pages'] = pages
    resp_data['current'] = 'food'
    resp_data['search_con'] = {
        'date_from': date_from,
        'date_to': date_to
    }
    return ops_render("stat/food.html", resp_data)

