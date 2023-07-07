ARG VARIANT="3.8"
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT} as builder

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    gcc \
    git

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN pip install toml

COPY projects/project-a/poetry.lock projects/project-a/pyproject.toml /shared/
COPY pyproject.toml /shared/pyproject_root.toml
COPY scripts /shared/scripts

RUN python3 /shared/scripts/merge_pyproject.py /shared/pyproject_root.toml /shared/pyproject.toml /shared/pyproject.toml --copy tool.poetry.group.dev.dependencies tool.black tool.mypy tool.isort


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
#COPY projects/project-a/poetry.lock projects/project-a/pyproject.toml /shared/
COPY --from=builder /shared/pyproject.toml /shared/poetry.lock /shared/

# Copy the shared package written in pyproject.toml
COPY shared/pkg1/ /shared/pkg1/

RUN poetry config virtualenvs.create false && \
    poetry lock --no-update && \
    poetry install --no-root
