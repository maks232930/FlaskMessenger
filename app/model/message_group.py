from sqlalchemy import Column, Boolean, Integer, Text

import app.model as model


class MessageGroup(model.BaseModel):
    chat_id = Column(Integer, ForeignKey('chat_group.id'), nullable=False)
    content = Column(Text, nullable=False)
    is_delete = Column(Boolean, default=False)
