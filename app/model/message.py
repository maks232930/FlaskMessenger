from sqlalchemy import Column, Boolean, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from .base import Base


class Message(Base):
    __tablename__ = 'messages'

    chat_id = Column(Integer, ForeignKey('chats.id', ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    read = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)

    chat = relationship("Chat", backref='chat_message')
