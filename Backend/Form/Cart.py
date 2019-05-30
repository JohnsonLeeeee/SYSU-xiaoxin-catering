from .Base import BaseForm as Form
from wtforms import StringField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, length, Email, Regexp

class SingleItemForm(Form):
    did = IntegerField(validators=[DataRequired()])
    quantity = IntegerField(validators=[DataRequired(),length(min=1,max=99,message="请在合理的数量范围内 1-99")])


class CartForm(Form):
    lists = FieldList(FormField(SingleItemForm))