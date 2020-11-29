from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, CHAR, Boolean, LargeBinary, String

from .base import Base
from app.extensions import ma


class User(Base, UserMixin):
    __tablename__ = 'users'
    username = Column(CHAR(150), unique=True, nullable=False)
    email = Column(CHAR(100), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_staff = Column(Boolean, default=False, nullable=False)
    phone = Column(CHAR(20), unique=True, nullable=False)
    avatar = Column(LargeBinary, nullable=True)

    # profile = relationship("Profile", uselist=False, back_populates='user')

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
