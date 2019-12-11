import re
import sys

project_name = '{{cookiecutter.project_name}}'

if not project_name:
    print('ERROR: The project name cannot be empty.')
    sys.exit(1)

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{cookiecutter.project_slug}}'

if not module_name:
    print('ERROR: The project slug cannot be empty.')
    sys.exit(1)

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name.' % module_name)
    sys.exit(1)
