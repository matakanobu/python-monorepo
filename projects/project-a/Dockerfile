FROM amd64/python:3.8.16-slim as builder

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

COPY ./poetry.lock ./pyproject.toml ./

# Copy the shared package written in pyproject.toml
COPY ./pkg1/ /shared/pkg1/

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --only main

FROM amd64/python:3.8.16-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

# Copy the installed packages from the builder image
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

WORKDIR /project
COPY src/ src/
COPY run.py .

CMD ["python", "run.py"]