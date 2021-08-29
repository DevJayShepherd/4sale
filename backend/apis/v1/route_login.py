from datetime import timedelta

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from backend.core.hashing import Hasher
from backend.core.security import create_access_token
from backend.db.repository.login import get_user_by_email
from backend.db.session import get_db
from backend.core.config import settings

router = APIRouter()


def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(email=email, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(plain_password=password, hashed_password=user.hashed_password):
        return False

    return user


@router.post("/token")
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                       db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect, email or password, please try again.")

    token_timeout = timedelta(minutes=int(settings.JWT_EXPIRATION))
    access_token = create_access_token(data={"sub": user.email}, expires_delta=token_timeout)

    return {"access_token": access_token, "token_type": "bearer"}
