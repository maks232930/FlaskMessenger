from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class MessageGroup(Base):
    chat_id = Column(Integer, ForeignKey('chat_group.id', ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    is_delete = Column(Boolean, default=False)

    chat = relationship("ChatGroup", backref='message_group_chat')
