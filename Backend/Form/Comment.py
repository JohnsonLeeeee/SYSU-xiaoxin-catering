# -*- coding:utf-8 -*-
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired
from wtforms.validators import length

from .Base import BaseForm as Form


class CommentForm(Form):
    uid = IntegerField(validators=[DataRequired()])
    content = StringField('评论', validators=[DataRequired(), length(min=2, max=100, message="内容不能超过100字符")])

