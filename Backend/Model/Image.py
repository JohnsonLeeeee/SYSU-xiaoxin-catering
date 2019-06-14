from ..Model.base import db


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    file_key = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
