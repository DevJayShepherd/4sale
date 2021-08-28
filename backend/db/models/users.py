import datetime
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from backend.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    facebook = Column(String, nullable=True)
    twitter = Column(String, nullable=True)
    website = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    public_email = Column(String, nullable=True)
    picture = Column(String, nullable=True)
    date_joined = Column(Date, default=datetime.datetime.now)
    property = relationship("Property", back_populates="owner")
