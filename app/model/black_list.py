from sqlalchemy import Column, Integer, ForeignKey

import app.model as model


class BlackList(model.BaseModel):
    __tablename__ = 'black_list'

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    black_id = Column(Integer, ForeignKey("user.id"), nullable=False)
