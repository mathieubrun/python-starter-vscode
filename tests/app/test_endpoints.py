from config import TestBase

from core.data import User


class TestUsersEndpoint(TestBase):
    def test_get_users(self, client, users_service):
        # arrange
        u = User(id=1, name="test", email="email")
        users_service.get_all.return_value = [u]

        # act
        response = client.get("/api/users")

        # assert
        assert response.status_code == 200
        assert "X-Request-ID" in response.headers
        assert response.json() == [u.model_dump()]
        users_service.get_all.assert_called_once()
