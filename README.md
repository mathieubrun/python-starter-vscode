## Dev environment

- VSCode : https://code.visualstudio.com/docs/languages/python
- Devcontainers : https://code.visualstudio.com/docs/devcontainers/containers
- Flake8 for linting : https://flake8.pycqa.org/en/latest/
- Debugger : `.vscode/launch.json` file
- Extensions 
  - git graph : https://github.com/mhutchie/vscode-git-graph 

## Logging

- Configuration using log.ini file : https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig

## Argument parsing

- See `cli_args.py` : https://docs.python.org/3/library/argparse.html

## Docker

``` sh
docker build -t starter-python .
docker run --rm -ti -p 8000:8000 starter-python
```

## Flask app

- See `app.py` : https://flask.palletsprojects.com/en/2.3.x/tutorial/

## Dependencies

See : https://github.com/jazzband/pip-tools

```
pip install -r requirements.txt
```

## Tests

Tests can be run either from Testing, either directly from test file. They can be debugged too. 
- See https://code.visualstudio.com/docs/python/testing
- See `app_test.py` : https://flask.palletsprojects.com/en/2.3.x/tutorial/tests/

### Code coverage

Code coverage is displayed on the left gutter, near line numbers
- See https://github.com/ryanluker/vscode-coverage-gutters
