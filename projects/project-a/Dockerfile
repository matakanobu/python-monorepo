FROM amd64/python:3.8.16-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./poetry.lock ./pyproject.toml ./

# Copy the shared package written in pyproject.toml
COPY ./pkg1/ /shared/pkg1/

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --only main

WORKDIR /project
COPY src/ src/
COPY run.py .

CMD ["python", "run.py"]