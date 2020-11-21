from sqlalchemy import Column, Boolean, Integer, ForeignKey

import app.model as model


class ChatParticipants(model.BaseModel):
    __tablename__ = 'chat_participant'

    chat_id = Column(Integer, ForeignKey('chat_group.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    is_admin = Column(Boolean, default=False)
