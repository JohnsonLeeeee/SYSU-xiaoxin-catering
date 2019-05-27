# -*- coding: utf-8 -*-
from flask import json
from flask import request
from flask import current_app
from werkzeug.exceptions import HTTPException
from werkzeug._compat import text_type


class APIException(HTTPException):
    code = 400
    error = 'invalid_request'
    error_code = 999
    headers = {}

    def __init__(self, error=None, error_code=None, code=None, headers=None,
                 response=None):
        if code is not None:
            self.code = code
        if error is not None:
            self.error = error
        if error_code is not None:
            self.error_code = error_code
        if headers is not None:
            headers_merged = headers.copy()
            headers_merged.update(self.headers)
            self.headers = headers_merged

        super(APIException, self).__init__(error, response)

    def get_body(self, environ=None):

        return text_type(json.dumps(dict(
            msg=self.error,
            code=self.error_code,
            request=request.method+'  '+self.get_url_no_param()
        ), ensure_ascii=False))

    # 截取url ‘?’ 前的路径
    def get_url_no_param(self):
        full_path = str(request.full_path)
        q_index = full_path.find('?')
        full_path = full_path[0:q_index]
        return full_path

    def get_headers(self, environ=None):
        return self.headers
        # return [('Content-Type', 'application/json')]


class FormError(APIException):

    # error_code=1000 means 参数错误
    def __init__(self, form, error='invalid_parameter', error_code=1000, response=None):
        self.form = form
        super(FormError, self).__init__(error, error_code, None, response)

    def get_body(self, environ=None):
        if current_app.config['SHOW_DETAIL_ERROR']:
            self.error = str(self.form.errors)
        return super().get_body(environ)
