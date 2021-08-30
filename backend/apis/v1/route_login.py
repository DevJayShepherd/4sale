from datetime import timedelta
from jose import jwt, JWTError

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
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


auth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


def get_current_user(token: str = Depends(auth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Not able to validate credentials")
    except JWTError:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="Not able to validate credentials")

    user = get_user_by_email(email=email, db=db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Not able to validate credentials")

    return user
