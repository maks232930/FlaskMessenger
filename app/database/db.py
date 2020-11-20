from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
