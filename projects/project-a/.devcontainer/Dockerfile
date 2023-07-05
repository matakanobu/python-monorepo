ARG VARIANT="3.8"
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT} as builder

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl \
    make

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /shared
COPY shared/pkg1/ /shared/pkg1/
RUN cd /shared/pkg1 && \
    poetry build


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
COPY --from=builder /shared/pkg1/dist/ /shared/pkg1/dist/

RUN cd /shared && \
    poetry export --without-hashes --with-credentials -f requirements.txt > requirements.txt && \
    pip install --no-cache --requirement requirements.txt