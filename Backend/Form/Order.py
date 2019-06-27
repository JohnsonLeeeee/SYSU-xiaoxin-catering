# -*- coding:utf-8 -*-
from wtforms import StringField
from wtforms import IntegerField
from wtforms import FieldList
from wtforms import FormField
from wtforms import DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import length

from .Base import BaseForm as Form
from .Cart import CartForm


class OrderForm(Form):
    uid = IntegerField(validators=[DataRequired()])
    total_price = DecimalField(validators=[DataRequired()])
    coupon_discount = DecimalField(validators=[DataRequired()])
    note = StringField('备注', validators=[DataRequired(), length(min=2, max=100, message="备注不能超过100字符")])
    rid = IntegerField(validators=[DataRequired()])
    lists = FieldList(FormField(CartForm))
