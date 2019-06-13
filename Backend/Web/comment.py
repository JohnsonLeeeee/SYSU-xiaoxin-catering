# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, redirect
from ..libs.web_help import ops_render, getCurrentDate, iPagination, getDictFilterField
from ..Model.base import db
from ..Config import settings
from ..Model.Comment import Comment
from ..libs.UrlManager import UrlManager
from ..Service.Food import FoodService
from ..Model.FoodStockChangeLog import FoodStockChangeLog
from decimal import Decimal
from sqlalchemy import or_
route_comment = Blueprint('comment', __name__, url_prefix='/comment')


@route_comment.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = Comment.query
    if 'mix_kw' in req:
        rule = or_(Comment.content.ilike("%{0}%".format(req['mix_kw'])), Comment.uid.ilike("%{0}%".format(req['mix_kw'])), Comment.rid.ilike("%{0}%".format(req['mix_kw'])))
        query = query.filter(rule)

    if 'status' in req and int(req['status']) > -1:
        query = query.filter(Comment.status == int(req['status']))

    if 'rid' in req and int(req['rid']) > 0:
        query = query.filter(Comment.rid == int(req['cid']))

    page_params = {
        'total': query.count(),
        'page_size': settings.PAGE_SIZE,
        'page': page,
        'display': settings.PAGE_DISPLAY,
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)
    offset = (page - 1) * settings.PAGE_SIZE
    list = query.order_by(Comment.id.desc()).offset(offset).limit(settings.PAGE_SIZE).all()

    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['status_mapping'] = settings.STATUS_MAPPING
    resp_data['current'] = 'index'
    return ops_render("comment/index.html", resp_data)


