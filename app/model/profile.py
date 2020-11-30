from sqlalchemy import Column, CHAR, Boolean, Text, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.extensions import ma
from .base import Base
from .user import User


class Profile(Base):
    __tablename__ = 'profiles'

    first_name = Column(CHAR(50), nullable=False)
    last_name = Column(CHAR(50), nullable=False)
    profile_description = Column(Text)
    date_of_birth = Column(Date)
    online = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)
    user = relationship(User, backref="profiles", lazy=True, uselist=False)


class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Profile


profile_schema = ProfileSchema()
