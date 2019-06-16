
from flask import jsonify, g

from Backend.libs.exception_api import  Success
from Backend.libs.MyBluePrint import MyBluePrint
from Backend.libs.auth import auth
from Backend.Model.base import db
from Backend.Model.Comment import Comment
from Backend.Form.Comment import CommentForm
from Backend.Viewmodel.Comment import CommentViewModel

api = MyBluePrint('comment')

@api.route('/<int:rid>', methods=['GET'])
@auth.login_required
def get_restaurant_comment(rid):
    comments = Comment.query.filter_by(rid=rid).all()
    list = [CommentViewModel.comment(i) for i in comments]
    return jsonify(comments = list, number = len(list))


@api.route('/<int:rid>', methods=['PUT','POST'])
@auth.login_required
def create_comment(rid):
    comment_info = CommentForm().validate_for_api()
    with db.auto_commit():
        comment = Comment()
        comment.content = comment_info.content.data
        comment.uid = comment_info.uid.data
        comment.rid = rid
        db.session.add(comment)
    return Success()