from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.schema.users import UserCreate, UserShow
from backend.db.session import get_db
from backend.db.repository.users import create_user


router = APIRouter()


@router.post("", response_model=UserShow)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_user(user, db)
    return user
