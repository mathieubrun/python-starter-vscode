from logging import debug
from typing import List

from dishka.integrations.fastapi import DishkaRoute, FromDishka, inject_sync
from fastapi import APIRouter

from core.config import PrimaryService
from core.data import User

router = APIRouter(prefix="/api", route_class=DishkaRoute)

# The router for endpoints that should be ignored in the OpenAPI schema
# (e.g., health checks, internal endpoints)
router_ignored = APIRouter(include_in_schema=False, route_class=DishkaRoute)


@router.get("/users", response_model=List[User])
@inject_sync
async def get_users(users: FromDishka[PrimaryService]):
    debug("get_users api called")
    return users.get_all()


@router_ignored.get("/fail")
@inject_sync
async def fail():
    return 5 / 0
