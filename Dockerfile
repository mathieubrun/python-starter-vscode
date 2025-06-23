FROM python:3.13-alpine AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

RUN uv run pytest

FROM python:3.13-alpine
COPY --from=builder --chown=app:app /app /app
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "src/api/log_config.yaml"]

