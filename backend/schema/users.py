from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: EmailStr
    facebook: Optional[str]
    twitter: Optional[str]
    website: Optional[str]
    phone: Optional[str]
    public_email: Optional[str]
    picture: Optional[str]


class UserShow(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    facebook: Optional[str]
    twitter: Optional[str]
    website: Optional[str]
    phone: Optional[str]
    public_email: Optional[str]
    picture: Optional[str]

    class Config:
        orm_mode = True
