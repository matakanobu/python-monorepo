TMP_DIR := $(shell mktemp -d)
REPO_NAME := project-a

default: build
.PHONY: build, test, run

build:
	# Copy project files
	cp -r src $(TMP_DIR)/src
	cp run.py $(TMP_DIR)
	cp Dockerfile .dockerignore $(TMP_DIR)
	cp pyproject.toml poetry.lock $(TMP_DIR)

	# Copy pkg1 files
	cp -r ../../shared/pkg1 $(TMP_DIR)/pkg1

	cd $(TMP_DIR)

	# Build pkg1
	cd $(TMP_DIR)/pkg1 && poetry build && cp -r dist ../dist && cd $(TMP_DIR)

	docker build -t $(REPO_NAME) $(TMP_DIR)

	rm -rf $(TMP_DIR)

test:
	poetry run python -m pytest tests

clean:
	docker rmi $(REPO_NAME)

run:
	docker run -it --rm $(REPO_NAME)
