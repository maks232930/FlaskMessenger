from sqlalchemy import Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship

from app.extensions import ma
from .base import Base
from .user import User


class Chat(Base):
    __tablename__ = 'chats'
    name = Column(VARCHAR, nullable=False)
    first_participant_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    second_participant_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False, unique=True)

    first_participant = relationship(User, post_update=True, foreign_keys=[first_participant_id],
                                     backref='first_user')
    second_participant = relationship(User, post_update=True, foreign_keys=[second_participant_id],
                                      backref='second_user')


class ChatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Chat


chat_schema = ChatSchema()
chats_schema = ChatSchema(many=True)
