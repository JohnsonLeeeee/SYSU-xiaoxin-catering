# -*- coding: utf-8 -*-
from flask import Blueprint,request
from ..libs.web_help import ops_render,getFormatDate,iPagination,getDictFilterField,selectFilterObj
from ..Service.StatisticsService import StatDailySite, StatDailyFood, StatDailyMember
from ..Model.Comment import Comment
from ..Config.settings import PAGE_DISPLAY, PAGE_SIZE
from ..Model.Dish import Dish as Food
import datetime

route_stat = Blueprint( 'stat_page',__name__ )

@route_stat.route( "/index" )
def index():
    now = datetime.datetime.now()
    date_before_30days = now + datetime.timedelta(days=-30)
    default_date_from = getFormatDate(date=date_before_30days, format="%Y-%m-%d")
    default_date_to = getFormatDate(date=now, format="%Y-%m-%d")

    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    date_from = req['date_from'] if 'date_from' in req else default_date_from
    date_to = req['date_to'] if 'date_to' in req else default_date_to
    query = StatDailySite.query.filter(StatDailySite.date >= date_from) \
        .filter(StatDailySite.date <= date_to)

    page_params = {
        'total': query.count(),
        'page_size': PAGE_SIZE,
        'page': page,
        'display': PAGE_DISPLAY,
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)
    offset = (page - 1) * PAGE_SIZE

    list = query.order_by(StatDailySite.id.desc()).offset( offset ).limit( PAGE_SIZE ).all()
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['current'] = 'index'
    resp_data['search_con'] = {
        'date_from':date_from,
        'date_to':date_to
    }
    return ops_render( "stat/index.html",resp_data )

@route_stat.route( "/food" )
def food():
    now = datetime.datetime.now()
    date_before_30days = now + datetime.timedelta(days=-30)
    default_date_from = getFormatDate(date=date_before_30days, format="%Y-%m-%d")
    default_date_to = getFormatDate(date=now, format="%Y-%m-%d")

    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    date_from = req['date_from'] if 'date_from' in req else default_date_from
    date_to = req['date_to'] if 'date_to' in req else default_date_to
    query = StatDailyFood.query.filter(StatDailyFood.date >= date_from) \
        .filter(StatDailyFood.date <= date_to)

    page_params = {
        'total': query.count(),
        'page_size': PAGE_SIZE,
        'page': page,
        'display': PAGE_DISPLAY,
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)
    offset = (page - 1) * PAGE_SIZE

    list = query.order_by(StatDailyFood.id.desc()).offset(offset).limit(PAGE_SIZE).all()
    date_list = []
    if list:
        food_map = getDictFilterField(Food, Food.id, "id", selectFilterObj(list, "food_id"))
        for item in list:
            tmp_food_info = food_map[item.food_id] if item.food_id in food_map else {}
            tmp_data = {
                "date": item.date,
                "total_count": item.total_count,
                "total_pay_money": item.total_pay_money,
                'food_info': tmp_food_info
            }
            date_list.append(tmp_data)

    resp_data['list'] = date_list
    resp_data['pages'] = pages
    resp_data['current'] = 'food'
    resp_data['search_con'] = {
        'date_from': date_from,
        'date_to': date_to
    }
    return ops_render( "stat/food.html",resp_data  )

@route_stat.route( "/member" )
def memebr():
    now = datetime.datetime.now()
    date_before_30days = now + datetime.timedelta(days=-30)
    default_date_from = getFormatDate(date=date_before_30days, format="%Y-%m-%d")
    default_date_to = getFormatDate(date=now, format="%Y-%m-%d")

    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    date_from = req['date_from'] if 'date_from' in req else default_date_from
    date_to = req['date_to'] if 'date_to' in req else default_date_to
    query = StatDailyMember.query.filter(StatDailyMember.date >= date_from) \
        .filter(StatDailyMember.date <= date_to)

    page_params = {
        'total': query.count(),
        'page_size': PAGE_SIZE,
        'page': page,
        'display': PAGE_DISPLAY,
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)
    offset = (page - 1) * PAGE_SIZE

    list = query.order_by(StatDailyMember.id.desc()).offset(offset).limit(PAGE_SIZE).all()
    date_list = []
    if list:
        member_map = getDictFilterField( Comment,Comment.id,"id",selectFilterObj( list ,"member_id") )
        for item in list:
            tmp_member_info = member_map[ item.member_id ] if item.member_id in member_map else {}
            tmp_data = {
                "date":item.date,
                "total_pay_money":item.total_pay_money,
                "total_shared_count":item.total_shared_count,
                'member_info':tmp_member_info
            }
            date_list.append( tmp_data )

    resp_data['list'] = date_list
    resp_data['pages'] = pages
    resp_data['current'] = 'member'
    resp_data['search_con'] = {
        'date_from': date_from,
        'date_to': date_to
    }
    return ops_render( "stat/member.html",resp_data  )

@route_stat.route( "/share" )
def share():
    now = datetime.datetime.now()
    date_before_30days = now + datetime.timedelta(days=-30)
    default_date_from = getFormatDate(date=date_before_30days, format="%Y-%m-%d")
    default_date_to = getFormatDate(date=now, format="%Y-%m-%d")

    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    date_from = req['date_from'] if 'date_from' in req else default_date_from
    date_to = req['date_to'] if 'date_to' in req else default_date_to
    query = StatDailySite.query.filter(StatDailySite.date >= date_from) \
        .filter(StatDailySite.date <= date_to)

    page_params = {
        'total': query.count(),
        'page_size': PAGE_SIZE,
        'page': page,
        'display': PAGE_DISPLAY,
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)
    offset = (page - 1) * PAGE_SIZE

    list = query.order_by(StatDailySite.id.desc()).offset(offset).limit(PAGE_SIZE).all()
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['current'] = 'food'
    resp_data['search_con'] = {
        'date_from': date_from,
        'date_to': date_to
    }
    return ops_render( "stat/share.html",resp_data  )
