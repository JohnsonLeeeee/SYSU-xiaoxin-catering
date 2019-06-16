from ..Model.user import User
class CommentViewModel:
    @classmethod
    def comment(cls,comment):
        return dict(
            content=comment.content,
            user=User.query.filter_by(id = comment.uid).first().username
        )

