from logging import getLogger
from typing import Dict, List

from .models import User


class InMemoryUserRepository:
    def __init__(self):
        self._users: Dict[int, User] = {}
        self._next_id: int = 1
        self._logger = getLogger(f"{self.__class__.__name__}")
        self.add(User(name="john", email="john@example.com"))

    def add(self, user: User) -> User:
        self._logger.debug("add")
        user.id = self._next_id
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def get_by_id(self, user_id: int) -> User:
        self._logger.debug("get_by_id")
        return self._users.get(user_id)

    def get_by_email(self, email: str) -> User:
        self._logger.debug("get_by_email")
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def get_all(self) -> List[User]:
        self._logger.debug("get_all")
        return list(self._users.values())
