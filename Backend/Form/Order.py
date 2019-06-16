from .Base import BaseForm as Form
from .Cart import CartForm
from wtforms import StringField, IntegerField, FieldList, FormField,DecimalField
from wtforms.validators import DataRequired, length, Email, Regexp

class OrderForm(Form):
    uid = IntegerField(validators=[DataRequired()])
    total_price = DecimalField(validators=[DataRequired()])
    coupon_discount = DecimalField(validators=[DataRequired()])
    note = StringField('备注',validators=[DataRequired(),length(min=2,max=100,message="备注不能超过100字符")])
    rid = IntegerField(validators=[DataRequired()])
    lists = FieldList(FormField(CartForm))