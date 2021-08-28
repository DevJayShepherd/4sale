from sqlalchemy.orm import Session

from backend.db.models.property import Property
from backend.schema.properties import PropertyCreate


def add_new_property(the_property: PropertyCreate, db: Session, owner_id: int):
    the_property = Property(**the_property.dict(), owner_id=owner_id)
    db.add(the_property)
    db.commit()
    db.refresh(the_property)
    return the_property


def retrieve_properties(db: Session):
    properties = db.query(Property).all()
    return properties


def update_property_by_id(property_id: int, the_property: PropertyCreate, db: Session):
    existing_property = db.query(Property).filter(Property.id == property_id)

    if not existing_property:
        return False

    the_property.__dict__.update(owner_id=1)
    existing_property.update(the_property.__dict__)
    db.commit()
    return True
