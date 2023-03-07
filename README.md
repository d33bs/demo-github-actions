# Demo - Github Actions

This repository helps demonstrate various [Github Actions](https://docs.github.com/en/actions) capabilities.

## Background

This repository simulates what a Python project might look like within Github. In addition to leveraging Github Actions, this project assumes the use of [Poetry](https://python-poetry.org/docs/) for Python environment management, [pytest](https://docs.pytest.org/) for Python testing, and [Dagger](https://docs.dagger.io/) for reproducibility with testing.

See the tree below for a brief description of directories and files.

```text
├── .github (used for Github Actions workflow specifications)
│   └── workflows
│       ├── 1.example-action.yml
│       ├── 2.run-python-file.yml
│       ├── 3.run-matrixed-pytest-ghactions.yml
│       └── 4.run-matrixed-pytest-dagger.yml
│
├── dagger (used for running Dagger actions)
│   └── run_tests.py
│
├── poetry.lock (used for Python environment references via Poetry)
├── pyproject.toml (used for Python environment specification via Poetry)
│
└── python_app (used for simulating a Python package or application)
    ├── __init__.py
    ├── main.py
    └── tests (used for simulating a Python package or application tests)
        └── test_main.py
```

## Overview of Actions

- [1.example-action.yml](.github/workflows/1.example-action.yml): demonstrates how to run a basic Github Actions workflow.
- [2.run-python-file.yml](.github/workflows/2.run-python-file.yml): demonstrates how to run a Python file while retaining environment consistency.
- [3.run-matrixed-pytest-ghactions.yml](.github/workflows/3.run-matrixed-pytest-ghactions.yml): demonstrates how to run matrixed Python versions for confirming passing pytest tests using Github Actions.
- [4.run-matrixed-pytest-dagger.yml](.github/workflows/4.run-matrixed-pytest-dagger.yml): demonstrates how to run matrixed Python versions for confirming passing pytest tests using Github Actions and Dagger together.
