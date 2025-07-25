import logging

from dishka import Scope
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI, Request
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from core import Container, create_dishka_container

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


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as exc:
            logging.exception("uncaught exception")
            return JSONResponse(
                status_code=500,
                content={"detail": f"{exc!r}."},
            )


def create_app(container: Container) -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    # Set up Dishka for dependency injection
    setup_dishka(container=container, app=app)

    # Include API routers
    # The main API router
    app.include_router(endpoints.router)
    # The router for endpoints that should be ignored in the OpenAPI schema
    # (e.g., health checks, internal endpoints)
    app.include_router(endpoints.router_ignored)

    # Add middleware for request ID logging
    # This middleware generates a unique ID for each request and makes it available
    # for logging and adds it as an 'X-Request-ID' header in the response.
    app.add_middleware(ExceptionMiddleware)
    app.add_middleware(log_config.RequestIdMiddleware)

    return app


fastapi_app = create_app(create_dishka_container(Scope.REQUEST))
