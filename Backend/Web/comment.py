# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from ..libs.web_help import ops_render, iPagination
from ..Config import settings
from ..Model.Comment import Comment
from ..Model.base import db
from sqlalchemy import or_
route_comment = Blueprint('comment', __name__, url_prefix='/comment')


@route_comment.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = Comment.query.filter(Comment.status != -9999)
    if 'mix_kw' in req:
        rule = or_(Comment.content.ilike("%{0}%".format(req['mix_kw'])), Comment.uid.ilike("%{0}%".format(req['mix_kw'])), Comment.rid.ilike("%{0}%".format(req['mix_kw'])),
                   Comment.status != -9999)
        query = query.filter(rule)

    if 'status' in req and int(req['status']) > -1:
        query = query.filter(Comment.status == int(req['status']))

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

@route_comment.route("/blacklist")
def blacklist():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = Comment.query

    query = query.filter(Comment.status == -9999)

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
    resp_data['current'] = 'blacklist'
    return ops_render("comment/blacklist.html", resp_data)


@route_comment.route("/ops",methods=["POST"])
def ops():
    resp = { 'code':200,'msg':'操作成功~~','data':{} }
    req = request.values

    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''

    if not id :
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号~~"
        return jsonify(resp)

    comment_info = Comment.query.filter_by(id = id).first()

    if not comment_info:
        resp['code'] = -1
        resp['msg'] = "指定评论不存在~~"
        return jsonify(resp)

    if act == "addblack":
        comment_info.status = -9999

    db.session.add(comment_info)
    db.session.commit()
    return jsonify( resp )



