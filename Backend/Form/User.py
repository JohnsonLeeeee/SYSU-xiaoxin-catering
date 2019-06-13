from .Base import BaseForm as Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp

class UserForm(Form):
    username = StringField('用户姓名',validators=[DataRequired(),length(min=2,max=10,message="用户姓名需要在2-10个字符之间")])
    phone = StringField('手机号', validators=[DataRequired(),
                                            Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])
    email = StringField('邮箱',validators=[DataRequired(),
                                            Regexp('^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$', 0, '请输入正确的邮箱地址')])

class ClientForm(UserForm):
    type = IntegerField('注册信息',validators=[DataRequired(),range(0,2)]) #使用邮箱或者手机


