# -*- coding:utf-8 -*-
from flask import current_app
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import FetchedValue
from sqlalchemy import Boolean
from sqlalchemy import String
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from sqlalchemy.orm import relationship
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from .base import db
from .user import User


class Adminstrator(User):
    __tablename__ = 'Adminstrator'

    rid = Column(Integer, ForeignKey('restaurant.id'), nullable=False, server_default=FetchedValue())
    restaurant = relationship('Restaurant')

    _pwd = Column('password', String(100))
    confirmed = Column(Boolean, default=False)

    @property
    def password(self):
        return self._pwd

    @password.setter
    def password(self, raw):
        self._pwd = generate_password_hash(raw)

    def check_pwd(self, raw):
        if not self._pwd:
            return False
        return check_password_hash(self._pwd, raw)

    @staticmethod
    def reset_password(id, new_pwd):
        admin = Adminstrator.query.get(id)
        if admin is None:
            return False
        admin.password = new_pwd
        db.session.commit()
        return True

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        # if data.get('id') != self.id:
        #     return False
        self.confirmed = True
        db.session.add(self)
        return True
