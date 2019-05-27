from .Base import BaseForm as Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp

class TokenForm(Form):
    token = StringField(validators=[DataRequired()])

class CartForm(Form):
    q = StringField(validators=[DataRequired()])