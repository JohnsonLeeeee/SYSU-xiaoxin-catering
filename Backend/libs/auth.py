
from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired

from.exception_api import AuthFailed, Forbidden
from .scope import is_in_scope


auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


import hashlib,requests,random,string,json
from ..Config.settings import MINA_APP


def getWeChatOpenId(code):
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
        .format(MINA_APP['appid'], MINA_APP['appkey'], code)
    r = requests.get(url)
    res = json.loads(r.text)
    openid = None
    session_key = None
    if 'openid' in res:
        openid = res['openid']
    if 'session_key' in res:
        session_key = res['session_key']
    return openid, session_key


@auth.verify_password
def verify_password(token, password):
    openid, session_key = getWeChatOpenId(token)
    return True
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        # request
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    # request 视图函数
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)
