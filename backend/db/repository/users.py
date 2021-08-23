from sqlalchemy.orm import Session

from backend.schema.users import UserCreate
from backend.db.models.users import User
from backend.core.hashing import Hasher


def create_user(user: UserCreate, db: Session):
    user = User(first_name=user.first_name,
                last_name=user.last_name,
                hashed_password=Hasher.get_password_hash(user.password),
                email=user.email,
                facebook=user.facebook,
                twitter=user.twitter,
                website=user.website,
                phone=user.phone,
                public_email=user.public_email,
                picture=user.picture)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
