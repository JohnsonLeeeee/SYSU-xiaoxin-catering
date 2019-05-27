from flask import current_app
from flask_login import UserMixin
from sqlalchemy.orm import relationship

from .base import db, Base
from sqlalchemy import Column, ForeignKey, func, BigInteger, FetchedValue
from sqlalchemy import String, Unicode, DateTime, Boolean
from sqlalchemy import SmallInteger, Integer, Float
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class User(UserMixin, Base):
    __tablename__ = 'user'

    uid = Column( BigInteger, primary_key=True)
    username =  Column( String(100), nullable=False, server_default= FetchedValue())
    address = relationship('Address')
    aid = Column(Integer, ForeignKey('address.id'), nullable=False, server_default=FetchedValue())
    phone_number =  Column( String(20),unique=True, nullable=False, server_default= FetchedValue())
    email =  Column( String(100), unique=True, nullable=False, server_default= FetchedValue())
    sex =  Column( Integer, nullable=False, server_default= FetchedValue())
    avatar =  Column( String(64), nullable=False, server_default= FetchedValue())
    _pwd =  Column( 'password', String(100))
    confirmed = Column(Boolean, default=False)


    @property
    def password(self):
        return self._pwd

    @password.setter
    def password(self,raw):
        self._pwd = generate_password_hash(raw)

    def check_pwd(self,raw):
        if not self._pwd:
            return False
        return check_password_hash(self._pwd,raw)

    @staticmethod
    def reset_password(token,new_pwd):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('id'))
        if user is None:
            return False
        user.password = new_pwd
        db.session.commit()
        return True

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')










