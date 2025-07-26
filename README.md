
# features

This starter kit is built with a modern, robust, and extensible set of tools and frameworks, making it suitable for a wide range of Python applications.

*   **Web API**: A high-performance asynchronous web API built with **[FastAPI](src/api/app.py)** and served by **Uvicorn**. It includes features like hot-reloading for development and configurable logging.

*   **API Client Collection**: Includes a **[Bruno](https://www.usebruno.com/)** collection in the **[bruno](bruno/)** directory, allowing for easy, code-based API testing.

*   **Command-Line Interface (CLI)**: A scriptable CLI, demonstrated in **[src/cli/main.py](src/cli/main.py)**, allowing for easy creation of terminal commands for automation, data processing, or administrative tasks.

*   **Dependency Injection with `dishka`**: Employs **`dishka`** for powerful and clean dependency injection across both the API and CLI.
    *   It showcases how to provide different service instances (`PrimaryService` for the API, `SecondaryService` for the CLI) from the same core logic (see **[src/core/config.py](src/core/config.py)**).
    *   Testing is made simple by allowing dependencies to be easily replaced with mocks (see **[tests/app/config.py](tests/app/config.py)**), ensuring components can be tested in isolation.

*   **Modern Python Tooling**: Utilizes **`uv`** as an extremely fast package manager. Project dependencies and scripts are managed in **[pyproject.toml](pyproject.toml)**.

*   **Containerization**: Comes with a **Dockerfile** for building and running the application in a containerized environment.

*   **Data Visualization & Apps**: Includes **Streamlit** as a dependency for building interactive applications.

*   **Structured Logging**: The API features a structured logging configuration (**src/api/log_config.yaml**).

# usage

## development

Format and lint :
````
ruff check --select I --fix
ruff format
````

## create venv

> uv sync

## debug

> use configured debug

## run locally

> uv run starter_cli

> uv run uvicorn api:app --reload --log-config src/api/log_config.yaml

## build docker

> docker build -t python-starter-kit .

> docker run --rm -ti -p 8000:8000 python-starter-kit
