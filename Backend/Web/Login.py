# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import redirect
from flask_login import current_user
import json

from ..Model.administrator import Adminstrator
from ..libs.web_help import ( ops_render )
from ..libs.UrlManager import ( UrlManager )
from ..Service.Login import LoginService
from ..Model.base import db
from ..Config.settings import AUTH_COOKIE_NAME

route_user = Blueprint('user', __name__)


@route_user.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "GET":
        return ops_render("user/edit.html", {'current': 'edit'})

    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    username = req['username'] if 'username' in req else ''
    email = req['email'] if 'email' in req else ''

    if username is None or len(username) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的姓名~~"
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的邮箱~~"
        return jsonify(resp)
    rid = Adminstrator.query.filter_by(id=current_user.id).first().rid
    user_info = Adminstrator.query.filter_by(id=current_user.id).first()
    user_info.username = username
    user_info.email = email
    user_info.rid = rid

    with db.auto_commit():
        db.session.add(user_info)
    return jsonify(resp)


@route_user.route("/reset-pwd", methods=["GET", "POST"])
def resetPwd():
    if request.method == "GET":
        return ops_render("user/reset_pwd.html", {'current': 'reset-pwd'})

    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values

    old_one = req['old_password'] if 'old_password' in req else ''
    if Adminstrator.query.filter_by(id=current_user.id).first().check_pwd(old_one) is False:
        resp['code'] = -1
        resp['msg'] = "请输入正确的原密码~~"
        return jsonify(resp)

    repeat_password = req['repeat_password'] if 'repeat_password' in req else ''
    new_password = req['new_password'] if 'new_password' in req else 'hhh'

    print(new_password)
    if new_password is None or len(new_password) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的新密码~~"
        return jsonify(resp)

    print(repeat_password, new_password)
    if repeat_password != new_password:
        resp['code'] = -1
        resp['msg'] = "两次密码输入不一致"
        return jsonify(resp)

    user_info = Adminstrator.query.filter_by(id=current_user.id).first()
    Adminstrator.reset_password(user_info.id, new_password)
    response = make_response(json.dumps(resp))
    response.set_cookie(AUTH_COOKIE_NAME, '%s#%s' % (
        LoginService.geneAuthCode(user_info), user_info.id), 60 * 60 * 24 * 120)  # 保存120天
    return response


@route_user.route("/logout")
def logout():
    response = make_response(redirect(UrlManager.buildUrl("/user/login")))
    response.delete_cookie(AUTH_COOKIE_NAME)
    return response
