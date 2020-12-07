from sqlalchemy import Column, VARCHAR, LargeBinary

from .base import Base


class ChatGroup(Base):
    __tablename__ = 'chats_groups'

    name = Column(VARCHAR(255), nullable=False)
    photo = Column(LargeBinary)
