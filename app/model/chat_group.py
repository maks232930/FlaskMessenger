from sqlalchemy import Column, CHAR, LargeBinary, ForeignKey, Integer

from .base import Base


class ChatGroup(Base):
    __tablename__ = 'chat_group'

    name = Column(CHAR(255), nullable=False)
    photo = Column(LargeBinary)

