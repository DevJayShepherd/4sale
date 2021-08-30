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


def retrieve_property_by_id(property_id: int, db: Session):
    the_property = db.query(Property).filter(Property.id == property_id).first()
    return the_property


def update_property_by_id(property_id: int, the_property: PropertyCreate, db: Session):
    existing_property = db.query(Property).filter(Property.id == property_id).first()

    if not existing_property:
        return False

    existing_property.property_title = the_property.property_title
    existing_property.property_price = the_property.property_price
    existing_property.property_status = the_property.property_status
    existing_property.property_area_size = the_property.property_area_size
    existing_property.property_bedrooms = the_property.property_bedrooms
    existing_property.property_garages = the_property.property_garages
    existing_property.property_bathrooms = the_property.property_bathrooms
    existing_property.property_description = the_property.property_description

    db.commit()
    return True


def delete_property_by_id(property_id: int, db: Session):
    the_property = db.query(Property).filter(Property.id == property_id)
    db.delete(the_property)
    db.commit()
    db.refresh(the_property)
    return "Successfully deleted"
