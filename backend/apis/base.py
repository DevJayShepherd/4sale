from fastapi import APIRouter

from backend.apis.v1 import route_users, route_property, route_login


api_router = APIRouter()

api_router.include_router(route_login.router, prefix="/login", tags=["login"])
api_router.include_router(route_users.router, prefix="/user", tags=["users"])
api_router.include_router(route_property.router, prefix="/property", tags=["properties"])

