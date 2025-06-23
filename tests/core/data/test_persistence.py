from pytest import fixture

from core.data import InMemoryUserRepository, User


class TestInMemoryUserRepository:
    @fixture
    def user_repo(self) -> InMemoryUserRepository:
        return InMemoryUserRepository()

    def test_add_user(self, user_repo: InMemoryUserRepository):
        user = User(name="Test User", email="test@example.com")
        added_user = user_repo.add(user)

        assert added_user.id == 2
        assert added_user.name == "Test User"

    def test_get_by_id(self, user_repo: InMemoryUserRepository):
        user = user_repo.get_by_id(1)
        assert user is not None
        assert user.id == 1
        assert user.name == "john"

    def test_get_by_id_not_found(self, user_repo: InMemoryUserRepository):
        non_existent_user = user_repo.get_by_id(999)
        assert non_existent_user is None

    def test_get_all(self, user_repo: InMemoryUserRepository):
        user1 = user_repo.add(User(name="User One", email="one@example.com"))
        user2 = user_repo.add(User(name="User Two", email="two@example.com"))
        all_users = user_repo.get_all()

        assert len(all_users) == 3
        assert user1 in all_users
        assert user2 in all_users
