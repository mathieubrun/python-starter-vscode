from unittest.mock import Mock

from pytest import fixture, raises

from core.data.models import User
from core.data.persistence import InMemoryUserRepository
from core.users.services import UsersService


class TestUsersService:
    @fixture
    def user_repository(self):
        return Mock()

    @fixture
    def sut(self, user_repository: InMemoryUserRepository) -> UsersService:
        return UsersService(repository=user_repository, name="test")

    def test_add_user_success(
        self,
        sut: UsersService,
        user_repository: InMemoryUserRepository,
    ):
        name = "Jane Doe"
        email = "jane.doe@example.com"
        user_repository.get_by_email.return_value = None

        _ = sut.add_user(name, email)

        user_repository.get_by_email.assert_called_once_with(email)
        user_repository.add.assert_called_once_with(User(name=name, email=email))

    def test_add_user_duplicate_email_raises_error(
        self,
        sut: UsersService,
        user_repository: InMemoryUserRepository,
    ):
        name = "Another John"
        email = "john@example.com"  # This email already exists
        user_repository.get_by_email.return_value = User(name="John Doe", email=email)

        with raises(ValueError, match=f"User with email {email} already exists"):
            _ = sut.add_user(name, email)

        user_repository.add.assert_not_called()
