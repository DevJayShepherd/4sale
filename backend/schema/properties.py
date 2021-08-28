from typing import Optional
from pydantic import BaseModel


class PropertyCreate(BaseModel):
    property_title: str
    property_price: str
    property_status: str
    property_area_size: str
    property_bedrooms: int
    property_garages: Optional[int] = 0
    property_bathrooms: int
    property_description: str


class PropertyShow(BaseModel):
    property_title: str
    property_price: str
    property_status: str
    property_area_size: str
    property_bedrooms: int
    property_garages: Optional[int] = 0
    property_bathrooms: int
    property_description: str

    class Config:
        orm_mode = True
