from sqlalchemy import Column, CHAR, Boolean, Text, Date, Integer, ForeignKey

import app.model as model


class Profile(model.BaseModel):
    __tablename__ = 'profile'

    first_name = Column(CHAR(50), nullable=False)
    last_name = Column(CHAR(50), nullable=False)
    profile_description = Column(Text)
    date_of_birth = Column(Date)
    online = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, unique=True)
