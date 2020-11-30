from sqlalchemy import Column, Boolean, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.extensions import ma
from .base import Base
from .chat import Chat
from .user import User


class Message(Base):
    __tablename__ = 'messages'

    chat_id = Column(Integer, ForeignKey('chats.id', ondelete="CASCADE"), nullable=False)
    sender_id = Column(Integer, ForeignKey('users.id', ondelete="SET NULL"), nullable=False)
    content = Column(Text, nullable=False)
    read = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)

    chat = relationship(Chat, backref='chat_message')
    sender = relationship(User, backref='chat_sender')


class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
