TMP_DIR := $(shell mktemp -d)
IMAGE_NAME := project-a

default: build
.PHONY: all, build, test, clean, run

all: build test run

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
	docker run --rm -it -v `pwd`/tests:/project/tests:ro --entrypoint /bin/bash $(IMAGE_NAME) -c 'pip install pytest; python -m pytest /project/tests'

# Remove the docker image
clean:
	docker rmi $(IMAGE_NAME)

# Run the docker container with arguments(if you need)
run:
	docker run -it --rm $(IMAGE_NAME)
