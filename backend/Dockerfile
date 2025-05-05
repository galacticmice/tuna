ARG PYTHON_VERSION=3.13.3
FROM python:${PYTHON_VERSION}-slim as base

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app

RUN uv sync --frozen --no-cache

EXPOSE 8080

CMD ["uv", "run", "uvicorn", "src.app:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
