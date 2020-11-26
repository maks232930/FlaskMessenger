from flask_login import UserMixin
from sqlalchemy import Column, CHAR, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

from .base import Base


class User(Base, UserMixin):
    __tablename__ = 'users'
    username = Column(CHAR(150), unique=True, nullable=False)
    email = Column(CHAR(100), unique=True, nullable=False)
    password_hash = Column(CHAR(255), nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_staff = Column(Boolean, default=False, nullable=False)
    phone = Column(CHAR(20), unique=True, nullable=False)
    avatar = Column(LargeBinary, nullable=True)

    # profile = relationship("Profile", uselist=False, back_populates='user')

    def __repr__(self):
        return f'User {self.username}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
