FROM tiangolo/uvicorn-gunicorn:python3.8

COPY pyproject.toml poetry.lock* ./
RUN python3.8 -m pip install poetry
RUN poetry config virtualenvs.create false && python3.8 -m poetry install --no-root --no-dev