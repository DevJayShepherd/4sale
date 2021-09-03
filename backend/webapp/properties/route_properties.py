from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.db.repository.properties import retrieve_properties, retrieve_property_by_id
from backend.db.session import get_db
from backend.core.s3 import get_s3_image_url


templates = Jinja2Templates(directory="backend/templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def homepage(request: Request, db: Session = Depends(get_db)):
    properties = retrieve_properties(db)
    for item in properties:
        item.image_url = get_s3_image_url(property_title=item.property_title)

    return templates.TemplateResponse("4sale/homepage.html", {"request": request,
                                                              "properties": properties})


@router.get("/property/{id}")
def property_page(id: int, request: Request, db: Session = Depends(get_db)):
    the_property = retrieve_property_by_id(property_id=id, db=db)
    the_property.image_url = get_s3_image_url(property_title=the_property.property_title)
    return templates.TemplateResponse("4sale/property.html", {"request": request,
                                                              "the_property": the_property})


@router.get("/signup")
def sign_up(request: Request):
    return templates.TemplateResponse("4sale/signup.html", {"request": request})
