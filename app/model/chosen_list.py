from sqlalchemy import Column, ForeignKey, Integer

import app.model as model


class ChosenList(model.BaseModel):
    __tablename__ = 'chosen_list'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    chosen_id = Column(Integer, ForeignKey('user.id'), nullable=False)
