FROM python:3.11

run pip install poetry

ENV DB_CONNECTION=pg\
    DB_HOST=127.0.0.1\
    DB_PORT=5432\
    DB_USER=rinha\
    DB_PASSWORD=rinha\
    DB_DATABASE=rinha\
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN touch README.md

RUN poetry install

ENTRYPOINT  ["poetry", "run", "python", "-m", "start.py"]

