ARG VARIANT="3.8"
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /shared
COPY projects/project-a/poetry.lock projects/project-a/pyproject.toml /shared/

# Copy the shared package written in pyproject.toml
COPY shared/pkg1/ /shared/pkg1/

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --only main
