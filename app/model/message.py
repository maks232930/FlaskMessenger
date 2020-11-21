from sqlalchemy import Column, Boolean, Integer, ForeignKey, Text

import app.model as model


class Message(model.BaseModel):
    __tablename__ = 'message'

    chat_id = Column(Integer, ForeignKey('chat.id'), nullable=False)
    content = Column(Text, nullable=False)
    read = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)
