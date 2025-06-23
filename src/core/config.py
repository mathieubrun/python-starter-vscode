from typing import Iterator, NewType

from dishka import Container, Provider, Scope, make_container, provide
from pydantic_settings import BaseSettings

from core.data import InMemoryUserRepository
from core.users.services import UsersService

PrimaryService = NewType("PrimaryService", UsersService)
SecondaryService = NewType("SecondaryService", UsersService)


class AppSettings(BaseSettings):
    APP_NAME: str = "Awesome API"
    ADMIN_EMAIL: str


class AppProvider(Provider):
    user_repository = provide(InMemoryUserRepository)

    @provide(scope=Scope.APP)
    def get_settings(self) -> AppSettings:
        """
        Provides the application settings object.
        Scope.APP ensures it's created only once per container.
        """
        return AppSettings()

    @provide()
    def get_primary_service(
        self, repository: InMemoryUserRepository
    ) -> Iterator[PrimaryService]:
        yield from self.get_user_service(repository, "primary")

    @provide()
    def get_secondary_service(
        self, repository: InMemoryUserRepository
    ) -> Iterator[SecondaryService]:
        yield from self.get_user_service(repository, "secondary")

    def get_user_service(
        # This method provides a UsersService instance with a request-level scope.
        # It demonstrates how to manage resources that require setup (login) and
        # teardown (logout) within the lifecycle of a request.
        self,
        repository: InMemoryUserRepository,
        name: str,
    ) -> Iterator[UsersService]:
        users_service = UsersService(repository, name)
        try:
            users_service.login()
            yield users_service
        finally:
            users_service.logout()


def create_dishka_container(scope: Scope) -> Container:
    return make_container(AppProvider(scope=scope))
