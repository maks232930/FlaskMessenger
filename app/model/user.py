from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, CHAR, Boolean, LargeBinary, String, VARCHAR

from app.extensions import ma
from .base import Base


class User(Base, UserMixin):
    __tablename__ = 'users'
    username = Column(VARCHAR(150), unique=True, nullable=False)
    email = Column(VARCHAR(100), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    _is_superuser = Column(Boolean, default=False, nullable=False)
    _is_staff = Column(Boolean, default=False, nullable=False)
    phone = Column(VARCHAR(20), unique=True, nullable=False)
    avatar = Column(LargeBinary, nullable=True)

    # profile = relationship("Profile", back_populates='user', uselist=False)

    @property
    def is_staff(self):
        return self._is_staff

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value

    @property
    def is_superuser(self):
        return self._is_superuser

    @is_superuser.setter
    def is_superuser(self, value):
        self._is_superuser = value

    def __repr__(self):
        return f'User {self.username}'

    def hash_password(self):
        self.password_hash = generate_password_hash(self.password_hash).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)
