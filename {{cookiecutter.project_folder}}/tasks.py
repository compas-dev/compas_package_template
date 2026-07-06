import os

from compas_invocations2 import build
from compas_invocations2 import mkdocs
from compas_invocations2 import style
from compas_invocations2 import tests
from invoke.collection import Collection

ns = Collection(
    style.check,
    style.lint,
    style.format,
    mkdocs.docs,
    tests.test,
    tests.testdocs,
    tests.testcodeblocks,
    build.prepare_changelog,
    build.clean,
    build.release,
    build.build_ghuser_components,
)
ns.configure(
    {
        "base_folder": os.path.dirname(__file__),
        "ghuser": {
            "source_dir": "src/{{ cookiecutter.project_slug }}/ghpython/components",
            "target_dir": "src/{{ cookiecutter.project_slug }}/ghpython/components/ghuser",
            "prefix": "{{ cookiecutter.project_slug }}: ",
        },
    }
)
