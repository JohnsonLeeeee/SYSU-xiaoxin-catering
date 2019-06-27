# -*- coding:utf-8 -*-
import json
import requests
from flask import g
from collections import namedtuple
from flask_httpauth import HTTPBasicAuth

from ..Config.settings import MINA_APP

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


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
