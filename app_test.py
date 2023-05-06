# Dependencies
from pytest import fixture

# Current project
from app import create_app


class TestApp:
    def test_get_root(self, client):
        response = client.get("/")
        assert b"Hello, World!" == response.data

    @fixture()
    def app(self):
        app = create_app()
        app.config.update(
            {
                "TESTING": True,
            }
        )

        # other setup can go here

        yield app

        # clean up / reset resources here

    @fixture()
    def client(self, app):
        return app.test_client()

    @fixture()
    def runner(self, app):
        return app.test_cli_runner()
