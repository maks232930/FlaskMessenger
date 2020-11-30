from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .chat_group import ChatGroup


class MessageGroup(Base):
    __tablename__ = 'messages_groups'
    chat_id = Column(Integer, ForeignKey('chats_groups.id', ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    is_delete = Column(Boolean, default=False)

    chat = relationship(ChatGroup, backref='message_group_chat')
