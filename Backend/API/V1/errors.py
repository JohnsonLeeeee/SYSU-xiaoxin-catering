'''
'''
from flask import render_template, request, jsonify, session
from datetime import timedelta

from app.libs.error_message import BaseException, UnknownException


@web.app_errorhandler(BaseException)
def api_error(e):
    args = e.get_args()
    http_code = args['http_code']
    response = jsonify(args['message'])
    # response.status_code = e.http_code
    return response, e.http_code


@web.app_errorhandler(404)
def page_not_found(e):
    """
        AOP，处理所有的404请求
    """
    return render_template('404.html'), 404


@web.app_errorhandler(500)
def internal_server_error(e):
    """
        AOP，处理所有的500请求
    """
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        unkown = UnknownException().get_args()
        response = jsonify(unkown['message'])
        response.status_code = 500
        return response
    return render_template('500.html'), 500

