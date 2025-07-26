import logging

from dishka import Scope
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI, Request
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import JSONResponse

from core import Container, create_dishka_container
from core.exceptions import CustomException

from . import endpoints, log_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan context manager.
    Handles startup and shutdown events for the application.
    """
    logging.debug("app : start")
    yield
    logging.debug("app : close container")
    app.state.dishka_container.close()
    logging.debug("app : stop")


def create_app(container: Container) -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    # Set up Dishka for dependency injection
    setup_dishka(container=container, app=app)

    # Include API routers
    app.include_router(endpoints.router)

    # Add middleware for request ID logging
    # This middleware generates a unique ID for each request and makes it available
    # for logging and adds it as an 'X-Request-ID' header in the response.
    # app.add_middleware(ExceptionMiddleware)
    app.add_middleware(log_config.RequestIdMiddleware)

    @app.exception_handler(CustomException)
    async def value_error_exception_handler(request: Request, exc: CustomException):
        logging.warning(exc.message)
        return JSONResponse(
            status_code=400,
            content={"detail": exc.message},
        )

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc: Exception):
        logging.error("uncaught exception")
        return JSONResponse(
            status_code=500,
            content={"detail": f"{exc!r}."},
        )

    return app


fastapi_app = create_app(create_dishka_container(Scope.REQUEST))
