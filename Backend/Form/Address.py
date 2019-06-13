from .Base import BaseForm as Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp

class AddressForm(Form):
    uid = IntegerField(validators=[DataRequired()])
    province_id = IntegerField(validators=[DataRequired()])
    city_id = IntegerField(validators=[DataRequired()])
    area_id = IntegerField(validators=[DataRequired()])
    address = StringField('具体地址', validators=[DataRequired(), length(min=1, max=20, message="内容不能超过20字符")])

