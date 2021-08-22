import datetime
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from backend.db.base_class import Base


class Property(Base):
    id = Column(Integer, primary_key=True, index=True)
    property_title = Column(String, nullable=False)
    property_price = Column(String, nullable=False)
    property_status = Column(String, nullable=False)
    property_area_size = Column(String, nullable=False)
    property_bedrooms = Column(Integer, nullable=False)
    property_garages = Column(Integer, nullable=False)
    property_bathrooms = Column(Integer, nullable=False)
    property_description = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    date_posted = Column(Date, nullable=False, default=datetime.datetime.now)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="property")



