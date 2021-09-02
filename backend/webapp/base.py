from fastapi import APIRouter
from backend.webapp.properties import route_properties

api_router = APIRouter()

api_router.include_router(route_properties.router, prefix="", tags=["homepage"])
