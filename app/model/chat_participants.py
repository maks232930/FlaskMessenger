from sqlalchemy import Column, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class ChatParticipants(Base):
    __tablename__ = 'chats_participants'

    chat_id = Column(Integer, ForeignKey('chats_groups.id', ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    is_admin = Column(Boolean, default=False)

    chat = relationship("ChatGroup", post_update=True, foreign_keys=[chat_id],
                        backref='chat')
    user = relationship("User", post_update=True, foreign_keys=[user_id],
                        backref='user')
