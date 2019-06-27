# -*- coding:utf-8 -*-
from wtforms import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange


class CartForm(Form):
    did = IntegerField(validators=[DataRequired()])
    quantity = IntegerField(validators=[DataRequired(),NumberRange(min=1, max=99, message="请在合理的数量范围内 1-99")])

