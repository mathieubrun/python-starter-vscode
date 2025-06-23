from logging import getLogger
from typing import List

from core.data.models import User
from core.data.persistence import InMemoryUserRepository


class UsersService:
    def __init__(self, repository: InMemoryUserRepository, name: str):
        self._repository = repository
        self._logger = getLogger(f"{self.__class__.__name__}.{name}")
        self._logger.debug("__init__")

    def add_user(self, name: str, email: str):
        self._logger.debug("add_user")
        user = User(name=name, email=email)

        if self._repository.get_by_email(email):
            raise ValueError(f"User with email {email} already exists")

        return self._repository.add(user)

    def get_all(self) -> List[User]:
        self._logger.debug("get_all")
        return self._repository.get_all()

    def login(self):
        self._logger.debug("login")

    def logout(self):
        self._logger.debug("logout")
