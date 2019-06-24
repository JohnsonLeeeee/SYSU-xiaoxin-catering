from datetime import datetime
from sqlalchemy import Column, SmallInteger, Integer, DateTime,func
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from flask import current_app
__all__ = ['db','Base']

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, throw = True):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e

class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    __abstract__ = True
    create_time = Column(DateTime(timezone=True), server_default=func.now() )
    status = Column(SmallInteger, default=1)
    update_time =  Column(DateTime(timezone=True), server_default=func.now() )

    def __getitem__(self, item):
        return getattr(self, item)

    def delete(self):
        self.status = 0

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id' and key != 'rid':
                setattr(self, key, value)

    def update(self):
        self.update_time = datetime.now()
        db.session.add(self)
        db.session.commit()


