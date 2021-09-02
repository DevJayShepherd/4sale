from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.db.repository.properties import retrieve_properties
from backend.db.session import get_db


templates = Jinja2Templates(directory="backend/templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def homepage(request: Request, db: Session = Depends(get_db)):
    properties = retrieve_properties(db)
    return templates.TemplateResponse("4sale/homepage.html", {"request": request,
                                                              "properties": properties})


@router.get("/signup")
def sign_up(request: Request):
    return templates.TemplateResponse("4sale/signup.html", {"request": request})
