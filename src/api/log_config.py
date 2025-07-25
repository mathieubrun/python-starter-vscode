from contextvars import ContextVar
from logging import Filter, LogRecord
from uuid import uuid4

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

id_length = 8
request_id_var: ContextVar[str] = ContextVar("request_id", default="_" * id_length)


class RequestIdLogFilter(Filter):
    """
    A logging filter that adds a request ID to log records.
    """

    def filter(self, record: LogRecord) -> bool:
        record.request_id = request_id_var.get()
        return True


class RequestIdMiddleware(BaseHTTPMiddleware):
    """
    Middleware to generate and attach a unique request ID to each incoming request.
    The request ID is stored in a ContextVar for logging purposes and
    added as an 'X-Request-ID' header in the response.
    """

    async def dispatch(self, request: Request, call_next):
        request_id = uuid4().hex[:id_length]

        request_id_var.set(request_id)
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
