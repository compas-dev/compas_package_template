# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

* Added `build` to template `requirements-dev.txt`.
* Added `.editorconfig`.
* Added `CHANGELOG.md`.
* Added `requirements.txt`.
* Added `tasks.py`.

### Changed

* Fixed import error for `Collection` from `invoke`.

### Removed

* Removed `black` from `pyproject.toml` of template repo.
* Removed `black` from `requirements-dev.txt` of template repo.
* Removed `_static` from docs folder of template repo.
* Removed `from __future__` imports from python files of template repo.
* Removed `HERE`, `HOME`, `DATA`, `DOCS`, `TEMP` from `__init__.py` of template repo package.
* Removed empty `data` and `temp` from template repo.
