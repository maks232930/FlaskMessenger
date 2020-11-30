from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .user import User


class BlackList(Base):
    __tablename__ = 'black_list'

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    black_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user = relationship(User, post_update=True, foreign_keys=[user_id],
                        backref='user')
    black = relationship(User, post_update=True, foreign_keys=[black_id],
                         backref='black_user')
