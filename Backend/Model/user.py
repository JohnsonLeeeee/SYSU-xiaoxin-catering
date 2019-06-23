from flask_login import UserMixin

from .base import db, Base
from sqlalchemy import Column, FetchedValue
from sqlalchemy import String,Integer

class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column( Integer, primary_key=True,autoincrement=True)
    openid = Column(String(100), nullable=True, server_default=FetchedValue()) #微信識別標識
    username =  Column( String(100), nullable=False, server_default= FetchedValue())
    email = Column(String(100), unique=True, server_default=FetchedValue())
    sex =  Column( Integer, default = 1, server_default= FetchedValue())
    avatar =  Column( String(64), server_default= FetchedValue())


    # def generate_token(self, expiration=600):
    #     s = Serializer(current_app.config['SECRET_KEY'], expiration)
    #     return s.dumps({'id': self.id}).decode('utf-8')

    # @staticmethod
    # def register_by_email(nickname, account, secret):
    #     with db.auto_commit():
    #         user = User()
    #         user.username = nickname
    #         user.email = account
    #         user.password = secret
    #         db.session.add(user)









