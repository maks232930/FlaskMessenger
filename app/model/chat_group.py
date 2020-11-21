from sqlalchemy import Column, CHAR, LargeBinary

import app.model as model


class ChatGroup(model.BaseModel):
    __tablename__ = 'chat_group'

    name = Column(CHAR(255), nullable=False)
    photo = Column(LargeBinary)
