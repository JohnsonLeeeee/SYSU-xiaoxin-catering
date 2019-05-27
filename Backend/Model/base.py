import datetime

from sqlalchemy import Column, SmallInteger, Integer, FetchedValue
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
__all__ = ['db','Base']

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
    update_time =  Column( 'update_time', Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def update(self):
        self.update_time = datetime.now()
        db.session.add(self)
        db.session.commit()
