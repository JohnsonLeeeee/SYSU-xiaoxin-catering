
from flask import jsonify, g

from Backend.libs.exception_api import DeleteSuccess, Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.user import User
from Backend.Form.User import UserForm,ClientForm

api = MyBluePrint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('/<int:uid>', methods=['PUT'])
def update_user():
    uid = g.user.uid
    userform = UserForm().validate_for_api()
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.username = userform.username.data
        user.phone_number = userform.phone.data
        user.update()
    return Success()


# @api.route('/register', methods=['POST'])
# def create_client():
#     form = ClientForm().validate_for_api()
#     promise = {
#         ClientTypeEnum.USER_EMAIL: __register_user_by_email,
#
#     }
#     promise[form.type.data]()
#     return Success()
#
#
# def __register_user_by_email():
#     form = UserEmailForm().validate_for_api()
#     User.register_by_email(form.nickname.data,
#                            form.account.data,
#                            form.secret.data)


