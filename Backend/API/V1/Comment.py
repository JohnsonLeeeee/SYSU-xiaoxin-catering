
from flask import jsonify, g

from Backend.libs.exception_api import  Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.Comment import Comment
from Backend.Form.Comment import CommentForm

api = MyBluePrint('comment')

@api.route('/<int:rid>', methods=['GET'])
@auth.login_required
def get_restaurant_comment(rid):
    comment = Comment.query.filter_by(rid=rid).all()
    return jsonify(comment)


@api.route('/<int:rid>', methods=['PUT','POST'])
@auth.login_required
def create_comment(rid):
    uid = g.user.uid
    comment_info = CommentForm().validate_for_api()
    with db.auto_commit():
        comment = Comment(uid=uid,rid=rid,content=comment_info.content)
        db.session.add(comment)
    return Success()