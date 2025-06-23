from unittest.mock import Mock

from dishka import Provider, Scope, make_container, provide
from fastapi.testclient import TestClient
from pytest import fixture

from api.app import create_app
from core.config import PrimaryService


class TestAppProvider(Provider):
    def __init__(self, mock_service, scope=None, component=None):
        super().__init__(scope, component)
        self.mock_service = mock_service

    @provide(scope=None)
    def users_service(self) -> PrimaryService:
        return self.mock_service


class TestBase:
    @fixture
    def client(self, users_service):
        return TestClient(
            create_app(
                make_container(TestAppProvider(users_service, scope=Scope.REQUEST))
            )
        )

    @fixture
    def users_service(self):
        return Mock()
