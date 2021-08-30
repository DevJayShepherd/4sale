from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.db.session import get_db
from backend.db.repository.properties import add_new_property, retrieve_properties, update_property_by_id, \
    retrieve_property_by_id, delete_property_by_id
from backend.schema.properties import PropertyCreate, PropertyShow
from backend.schema.common import DetailResponse
from backend.apis.v1.route_login import get_current_user


router = APIRouter()


@router.post("/create_property", response_model=PropertyShow)
def add_property(the_property: PropertyCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    owner_id = current_user.id
    the_property = add_new_property(the_property, db, owner_id=owner_id)
    return the_property


@router.get("/retrieve_all", response_model=List[PropertyShow])
def retrieve_all_properties(db: Session = Depends(get_db)):
    properties = retrieve_properties(db)
    return properties


@router.put("/edit_property/{id}", response_model=DetailResponse)
def edit_the_property(id: int, the_property: PropertyCreate, db: Session = Depends(get_db),
                      current_user=Depends(get_current_user)):

    existing_property = retrieve_property_by_id(id, db)
    if existing_property is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Property with id: {id} does not exist.")

    if existing_property.owner_id == current_user.id:
        update_property_by_id(property_id=id, the_property=the_property, db=db)
        return {"detail": "Successfully updated."}

    return {"detail": "Not authorized."}


@router.delete("delete_property/{id}")
def delete_property(property_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    owner_id = current_user.id

    the_property = retrieve_property_by_id(property_id, db)
    if not the_property:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Property with id: {id} does not exist.")

    if the_property.owner_id == owner_id:
        delete_property_by_id(property_id, db)
        return {"detail": f"Property with id: {id} has been deleted."}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not permitted.")
