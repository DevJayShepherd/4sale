from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.core.config import settings
from backend.db.session import engine

from backend.db.base import Base
from backend.db.base_class import Base
from backend.apis.base import api_router
from backend.webapp.base import api_router as webapp_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="backend/static"), name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    configure_static(app)
    return app


app = start_application()
