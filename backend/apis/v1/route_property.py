from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.session import get_db
from backend.db.models.property import Property
from backend.db.repository.properties import add_new_property
from backend.schema.properties import PropertyCreate, PropertyShow

router = APIRouter()


@router.post("/create-property", response_model=PropertyShow)
def add_property(the_property: PropertyCreate, db: Session = Depends(get_db)):
    owner_id = 1
    the_property = add_new_property(the_property, db, owner_id=owner_id)
    return the_property
