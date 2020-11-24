from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base


class ChosenList(Base):
    __tablename__ = 'chosen_list'

    user_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    chosen_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"), nullable=False)

    user = relationship("User", post_update=True, foreign_keys=[user_id],
                        backref='user')
    chosen = relationship("User", post_update=True, foreign_keys=[chosen_id],
                          backref='chosen_user')
