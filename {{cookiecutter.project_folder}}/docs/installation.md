# Installation

## Stable

Stable releases are available on PyPI and can be installed with pip.

```bash
pip install {{ cookiecutter.project_slug }}
```

## Latest

The latest version can be installed from local source.

```bash
git clone https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e .
```

## Development

To install `{{ cookiecutter.project_slug }}` for development, install from local source with the "dev" requirements.

```bash
git clone https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e .[dev]
```
