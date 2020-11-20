from sqlalchemy import Column, CHAR, Boolean, LargeBinary, Text, Date, Integer, ForeignKey

from app.database.db import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    username = Column(CHAR(150), unique=True, nullable=False)
    email = Column(CHAR(100), unique=True, nullable=False)
    password = Column(CHAR(100), nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    phone = Column(CHAR(20), unique=True, nullable=False)
    avatar = Column(LargeBinary, nullable=True)


class Profile(BaseModel):
    __tablename__ = 'profile'

    first_name = Column(CHAR(50), nullable=False)
    last_name = Column(CHAR(50), nullable=False)
    profile_description = Column(Text)
    date_of_birth = Column(Date)
    online = Column(Boolean, default=False)
    user = Column(Integer, ForeignKey('user.id'), uselist=False, nullable=False)


class ChosenList(BaseModel):
    __tablename__ = 'chosen_list'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    chosen_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class BlackList:
    __tablename__ = 'black_list'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    black_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class Chat(BaseModel):
    __tablename__ = 'chat'
    name = Column(CHAR(255), nullable=False)
    first_participant = Column(Integer, ForeignKey('user.id'), nullable=False)
    second_participant = Column(Integer, ForeignKey('user.id'), nullable=False)


class Message(BaseModel):
    __tablename__ = 'message'

    chat_id = Column(Integer, ForeignKey('chat.id'), nullable=False)
    content = Column(Text, nullable=False)
    read = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)


class ChatGroup(BaseModel):
    __tablename__ = 'chat_group'

    name = Column(CHAR(255), nullable=False)
    photo = Column(LargeBinary)


class MessageGroup(BaseModel):
    chat_id = Column(Integer, ForeignKey('chat_group.id'), nullable=False)
    content = Column(Text, nullable=False)
    is_delete = Column(Boolean, default=False)


class ChatParticipants(BaseModel):
    __tablename__ = 'chat_participant'

    chat_id = Column(Integer, ForeignKey('chat_group.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    is_admin = Column(Boolean, default=False)
