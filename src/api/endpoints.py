from logging import debug
from typing import List

from dishka.integrations.fastapi import DishkaRoute, FromDishka, inject_sync
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from core.config import PrimaryService
from core.data import User
from core.exceptions import CustomException

router = APIRouter(prefix="/api", route_class=DishkaRoute)


@router.get("/users", response_model=List[User])
@inject_sync
async def get_users(users: FromDishka[PrimaryService]):
    debug("get_users api called")
    return users.get_all()


@router.get("/exceptions/unhandled", include_in_schema=False)
@inject_sync
async def exceptions_unhandled():
    return 5 / 0


@router.get("/exceptions/http", include_in_schema=False)
@inject_sync
async def exceptions_http():
    raise HTTPException(status_code=400, detail="some error")


@router.get("/exceptions/custom", include_in_schema=False)
@inject_sync
async def exceptions_value():
    raise CustomException("test")
