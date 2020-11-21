from sqlalchemy import Column, CHAR, Integer, ForeignKey

import app.model as model


class Chat(model.BaseModel):
    __tablename__ = 'chat'
    name = Column(CHAR(255), nullable=False)
    first_participant = Column(Integer, ForeignKey('user.id'), nullable=False)
    second_participant = Column(Integer, ForeignKey('user.id'), nullable=False)
