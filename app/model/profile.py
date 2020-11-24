from sqlalchemy import Column, CHAR, Boolean, Text, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Profile(Base):
    __tablename__ = 'profile'

    first_name = Column(CHAR(50), nullable=False)
    last_name = Column(CHAR(50), nullable=False)
    profile_description = Column(Text)
    date_of_birth = Column(Date)
    online = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False, unique=True)
    user = relationship("User", back_populates="profiles")
