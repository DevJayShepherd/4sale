from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.db.session import get_db
from backend.db.repository.properties import add_new_property, retrieve_properties, update_property_by_id
from backend.schema.properties import PropertyCreate, PropertyShow
from backend.schema.common import DetailResponse
from typing import List

router = APIRouter()


@router.post("/create_property", response_model=PropertyShow)
def add_property(the_property: PropertyCreate, db: Session = Depends(get_db)):
    owner_id = 1
    the_property = add_new_property(the_property, db, owner_id=owner_id)
    return the_property


@router.get("/retrieve_all", response_model=List[PropertyShow])
def retrieve_all_properties(db: Session = Depends(get_db)):
    properties = retrieve_properties(db)
    return properties


@router.put("edit_property/{id}", response_model=DetailResponse)
def edit_the_property(id: int, the_property: PropertyCreate, db: Session = Depends(get_db)):
    owner_id = 1
    response = update_property_by_id(property_id=id, the_property=the_property, db=db, owner_id=owner_id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id: {id} does not exist.")
    return {"detail": "Successfully updated."}
