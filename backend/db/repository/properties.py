from sqlalchemy.orm import Session

from backend.db.models.property import Property
from backend.schema.properties import PropertyCreate


def add_new_property(the_property: PropertyCreate, db: Session, owner_id: int):
    the_property = Property(**the_property.dict(), owner_id=owner_id)
    db.add(the_property)
    db.commit()
    db.refresh(the_property)
    return the_property
