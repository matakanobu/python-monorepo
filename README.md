# python-monorepo

This repository is a monorepo example using Poetry. It manages multiple projects in a single repository and shares common code between the projects.

## Directory Structure

The repository has the following directory structure:

```
python-monorepo
├── .flake8
├── README.md
├── poetry.lock
├── pyproject.toml
├── projects
│   ├── project-a
│   │   ├── Dockerfile
│   │   ├── Makefile
│   │   ├── poetry.lock
│   │   ├── pyproject.toml
│   │   ├── run.py
│   │   ├── src
│   │   │   ├── __init__.py
│   │   │   └── pipeline.py
│   │   └── tests
│   │       ├── __init__.py
│   │       └── test_pipeline.py
│   └── project-b
│       ├── src
│       │   └── __init__.py
│       └── tests
│           └── __init__.py
└── shared
    ├── pkg1
    │   ├── __pycache__
    │   ├── pkg1
    │   │   ├── __init__.py
    │   │   └── base_pipeline.py
    │   ├── poetry.lock
    │   └── pyproject.toml
    └── pkg2
        ├── pkg2
        │   ├── __init__.py
        │   └── calc.py
        ├── poetry.lock
        └── pyproject.toml
```
* `projects`: Directory for storing individual projects.
* `shared`: Directory for packaging code shared across multiple projects.

## Use Cases

This monorepo is intended to serve the following use cases:
* Manage dependencies with Poetry.
* Manage multiple projects in a single repository.
* Share common code that is not dependent on a specific project.
* Deploy each project as a Docker image.
* Develop using a Devcontainer also.

## Concept

* Manage python package dependencies using pyproject.toml in each directory.
* Package the shared code in the shared directory and reference it from each project.
* Use relative paths to reference the common code without making it a wheel package.
* Use Makefile and Dockerfile to manage the procedure for setting up development environment and building deployment images.

## Usage

Development:
```bash
cd projects/project-xxx
make dep
```
or use a Devcontainer.

Deployment:
```bash
cd projects/project-xxx
make build
```

## Testing

```bash
cd projects/project1-xxx
petry run python -m pytest
```
or

Run tests inside a Docker container:
```bash
cd projects/project1-xxx
make test
```
