# Standard Library
from logging import getLogger

# Dependencies
from flask import Flask


def create_app() -> Flask:
    log = getLogger(f"{__name__}")
    log.info("Creating app")

    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "Hello, World!"

    log.info("Done")
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
