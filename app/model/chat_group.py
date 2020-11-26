from sqlalchemy import Column, CHAR, LargeBinary

from .base import Base


class ChatGroup(Base):
    __tablename__ = 'chats_groups'

    name = Column(CHAR(255), nullable=False)
    photo = Column(LargeBinary)
