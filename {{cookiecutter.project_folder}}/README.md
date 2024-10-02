# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Installation

Stable releases can be installed from PyPI.

```bash
pip install {{ cookiecutter.project_slug }}
```

To install the latest version for development, do:

```bash
git clone https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e ".[dev]"
```

## Documentation

For further "getting started" instructions, a tutorial, examples, and an API reference,
please check out the online documentation here: [{{ cookiecutter.project_name }} docs](https://{{ cookiecutter.github_organization }}.github.io/{{ cookiecutter.project_slug }})

## Issue Tracker

If you find a bug or if you have a problem with running the code, please file an issue on the [Issue Tracker](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}/issues).
