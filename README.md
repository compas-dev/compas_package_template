# COMPAS package template

Cookiecutter template for COMPAS extensions.

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html#)
is a command-line utility that lets you quickly bootstrap a new project from a template.
It takes a directory tree and copies it into your new project,
replacing all the generic info that finds surrounded by templating tags `{{` and `}}` with your project info written in `cookiecutter.json`.

## Features

* Project directory and file structure
* Documentation based on [Sphinx](http://www.sphinx-doc.org/en/master/)/[reStructuredText](http://docutils.sourceforge.net/rst.html)
* Testing framework: [pytest](https://docs.pytest.org/en/latest/)
* Basic setup script to create pip installable packages
* Automation of common tasks for development workflow based on [pyinvoke](http://www.pyinvoke.org/) (generate documentation, run tests, check format, etc.)
* [EditorConfig](https://editorconfig.org/) integration
* Minimal Github workflows for CI/CD

## What's included

* `.github`
* `data`
* `docs`
* `examples`
* `src`
* `temp`
* `tests`
* `.bumpversion.cfg`
* `.editorconfig`
* `.gitignore`
* `AUTHORS.md`
* `CHANGELOG.md`
* `CONTRIBUTING.md`
* `LICENSE`
* `MANIFEST.in`
* `pytest.ini`
* `README.md`
* `requirements-dev.txt`
* `requirements.txt`
* `setup.cfg`
* `setup.py`
* `tasks.py`

## Requirements

Install `cookiecutter` command line: `pip install cookiecutter`

## Usage

In the terminal, go to the folder where you want to place your project:

```bash
cd <your-projects-folder>
```

Generate a new Cookiecutter template layout:

```bash
cookiecutter gh:compas-dev/tpl-extension
```

Go to project folder:

```bash
cd <project-slug>
```

## Additional settings

To use the coding style feature with [EditorConfig](https://editorconfig.org/):

* Some text editors have a native EditorConfig.
  If yours doesn't you can download the appropriate plugin [here](https://editorconfig.org/#download).

## Github Actions
Basic CI/CD has already been setup in the .github folder, including automatic building test cross systems, documentation generation etc. There are few additional settings can be enabled manually.

### Enable Automatic Publishing to PYPI
Firstly add your PYPI token in repo secrets, then go to [.github/workflows/release.yaml]({{cookiecutter.project_folder}}/.github/workflows/release.yml) and uncomment Lines 28~48

### Enable versioning drop down list on documentation site
In [docs/conf.py]({{cookiecutter.project_folder}}/docs/conf.py), fill in correct URL and uncomment Lines 104~107

## License
This template is licensed under the terms of the [MIT License](/LICENSE)
