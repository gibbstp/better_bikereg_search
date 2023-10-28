FROM python:3.11-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip && \
    pip install poetry==1.6.1
    
ENV POETRY_HOME="/app/bin/poetry" \    
    POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml ./

RUN poetry install