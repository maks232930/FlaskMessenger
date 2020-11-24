from sqlalchemy import Column, CHAR, Boolean, LargeBinary
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = 'user'

    username = Column(CHAR(150), unique=True, nullable=False)
    email = Column(CHAR(100), unique=True, nullable=False)
    password = Column(CHAR(100), nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_staff = Column(Boolean, default=False, nullable=False)
    phone = Column(CHAR(20), unique=True, nullable=False)
    avatar = Column(LargeBinary, nullable=True)

    profile = relationship("Profile", uselist=False, back_populates='user')
    # black_list = relationship('BlackList', back_populates='user', cascade="all, delete-orphan")
    # chat = relationship('Chat', back_populates='user', cascade="all, delete-orphan")
    # chosen_list = relationship('ChosenList', back_populates='user', cascade="all, delete-orphan")
