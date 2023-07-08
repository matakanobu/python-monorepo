TMP_DIR := $(shell mktemp -d)
IMAGE_NAME := project-a
VENV_NAME := .venv_TMP

default: build
.PHONY: all, dev, build, test, clean, run

all: build test run

# Install the dependencies for development
dev:
	python3 -m venv $(VENV_NAME) && \
	$(VENV_NAME)/bin/pip install toml && \
	$(VENV_NAME)/bin/python merge_pyproject.py ../../pyproject.toml ./pyproject.toml ./pyproject.toml --copy tool.poetry.group.dev.dependencies tool.black tool.mypy tool.isort && \
	rm -rf $(VENV_NAME)
	poetry lock && poetry check && poetry install
	cp ../../.flake8 ./.flake8

# Build the docker image for deployment this project
build:
	# Copy project files
	cp -r src $(TMP_DIR)/src
	cp run.py $(TMP_DIR)
	cp Dockerfile .dockerignore $(TMP_DIR)
	cp pyproject.toml poetry.lock $(TMP_DIR)

	# Copy the shared package written in pyproject.toml
	cp -r ../../shared/pkg1 $(TMP_DIR)/pkg1

	docker build -t $(IMAGE_NAME) $(TMP_DIR)

	rm -rf $(TMP_DIR)

# Run the tests in the docker container
test:
	docker run --rm -it -v `pwd`/tests:/project/tests:ro --entrypoint /bin/bash $(IMAGE_NAME) -c 'pip install pytest; python -m pytest -vv /project/tests'

# Remove the docker image
clean:
	docker rmi $(IMAGE_NAME)

# Run the docker container with arguments(if you need)
run:
	docker run -it --rm $(IMAGE_NAME)
