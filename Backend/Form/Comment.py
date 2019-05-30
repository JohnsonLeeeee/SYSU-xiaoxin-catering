from .Base import BaseForm as Form
from wtforms import StringField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, length, Email, Regexp

class CommentForm(Form):
    rid = IntegerField(validators=[DataRequired()])
    uid = IntegerField(validators=[DataRequired()])
    content = StringField('评论', validators=[DataRequired(), length(min=2, max=100, message="内容不能超过100字符")])

