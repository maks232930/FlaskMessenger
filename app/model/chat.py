from sqlalchemy import Column, CHAR, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Chat(Base):
    __tablename__ = 'chats'
    name = Column(CHAR(255), nullable=False)
    first_participant_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    second_participant_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    first_participant = relationship("User", post_update=True, foreign_keys=[first_participant_id],
                                     backref='chat_first_participant')
    second_participant = relationship("User", post_update=True, foreign_keys=[second_participant_id],
                                      backref='chat_second_participant')
