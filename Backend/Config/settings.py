# -*- coding:utf-8 -*-
SHOW_DETAIL_ERROR = True

AUTH_COOKIE_NAME = "xiaoxin"
PAGE_SIZE = 50
PAGE_DISPLAY = 10


MINA_APP = {
    'appid': 'xxxxx',
    'appkey': 'xxxxxxxxxxxxx',
    'paykey': 'xxxxxxxxxxxxxx',
    'mch_id': 'xxxxxxxxxxxx',
    'callback_url': '/v1/order/callback'
}


STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}

PAY_STATUS_MAPPING = {
    "1": "已支付",
    "-8": "待支付",
    "0": "已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价"
}
