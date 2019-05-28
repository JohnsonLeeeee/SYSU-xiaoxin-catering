from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201

class DishCategory(Enum):
    """交易状态"""
    Dessert = 1
    Drink = 2
    Chinese = 3
    Western = 4

    @classmethod
    def category_str(cls, status):
        key_map = {
            cls.Dessert: {
                '甜品小吃'
            },
            cls.Drink: {
                '饮料'
            },
            cls.Chinese: {
                '中餐'
            },
            cls.Western: {
               '西餐'
            }
        }
        return key_map[status]