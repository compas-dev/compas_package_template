# flake8: noqa
# -*- coding: utf-8 -*-

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = "1.0"

import inspect
import importlib
import re
import sphinx_compas_theme  # this is a temp solution

# -- General configuration ------------------------------------------------

project = "{{ cookiecutter.project_name }}"
copyright = "{{ cookiecutter.copyright }}"
author = "{{ cookiecutter.author_name }}"


def get_latest_version():
    with open("../CHANGELOG.md", "r") as file:
        content = file.read()
        pattern = re.compile(r"## (Unreleased|\[\d+\.\d+\.\d+\])")
        versions = pattern.findall(content)
        latest_version = versions[0] if versions else None
        if (
            latest_version
            and latest_version.startswith("[")
            and latest_version.endswith("]")
        ):
            latest_version = latest_version[1:-1]
        return latest_version


latest_version = get_latest_version()
if latest_version == "Unreleased":
    release = "Unreleased"
    version = "latest"
else:
    release = latest_version
    version = ".".join(release.split(".")[0:2])

master_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
templates_path = sphinx_compas_theme.get_autosummary_templates_path() + ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints", "_notebooks", "**/__temp"]

# pygments_style = "sphinx"
# pygments_dark_style = "monokai"
# show_authors = True
add_module_names = True
language = "en"


# -- Extension configuration ------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    # "sphinx.ext.linkcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.coverage",
    # "sphinx.ext.inheritance_diagram",
    "sphinx.ext.graphviz",
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.autodoc.typehints",
    "sphinx_design",
    "sphinx_inline_tabs",
    "sphinx_togglebutton",
    "sphinx_remove_toctrees",
    "sphinx_copybutton",
    # "sphinxcontrib.bibtex",
    "numpydoc",
]

# remove_from_toctrees = ["api/generated/*"]

numpydoc_show_class_members = False
numpydoc_class_members_toctree = False
numpydoc_attributes_as_param_list = True

# bibtex options

# bibtex_bibfiles = ['refs.bib']

# autodoc options

autodoc_type_aliases = {}

# this does not work properly yet
# autodoc_typehints = "none"
# autodoc_typehints_format = "short"
autodoc_typehints_description_target = "documented"

autodoc_mock_imports = [
    "System",
    "clr",
    "Eto",
    "Rhino",
    "Grasshopper",
    "scriptcontext",
    "rhinoscriptsyntax",
    "bpy",
    "bmesh",
    "mathutils",
]

autodoc_default_options = {
    "undoc-members": True,
    "show-inheritance": True,
}

autodoc_member_order = "groupwise"

autoclass_content = "class"


def skip(app, what, name, obj, would_skip, options):
    if name.startswith("_"):
        return True
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)


# autosummary options

autosummary_generate = True
autosummary_mock_imports = [
    "System",
    "clr",
    "Eto",
    "Rhino",
    "Grasshopper",
    "scriptcontext",
    "rhinoscriptsyntax",
    "bpy",
    "bmesh",
    "mathutils",
]

# graph options

# plot options

plot_include_source = False
plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = ["png"]

# intersphinx options

intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "compas": ("https://compas.dev/compas/latest/", None),
}

# linkcode


def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    if not info["fullname"]:
        return None

    package = info["module"].split(".")[0]
    if not package.startswith('{{ cookiecutter.project_slug }}'):
        return None

    module = importlib.import_module(info["module"])
    parts = info["fullname"].split(".")

    if len(parts) == 1:
        obj = getattr(module, info["fullname"])
        mod = inspect.getmodule(obj)
        if not mod:
            return None
        filename = mod.__name__.replace(".", "/")
        lineno = inspect.getsourcelines(obj)[1]
    elif len(parts) == 2:
        obj_name, attr_name = parts
        obj = getattr(module, obj_name)
        attr = getattr(obj, attr_name)
        if inspect.isfunction(attr):
            mod = inspect.getmodule(attr)
            if not mod:
                return None
            filename = mod.__name__.replace(".", "/")
            lineno = inspect.getsourcelines(attr)[1]
        else:
            return None
    else:
        return None

    return f"https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}/blob/master/src/{filename}.py#L{lineno}"


# extlinks


extlinks = {
    "rhino": ("https://developer.rhino3d.com/api/RhinoCommon/html/T_%s.htm", "%s"),
    "blender": ("https://docs.blender.org/api/2.93/%s.html", "%s"),
}

# from pytorch

from sphinx.writers import html, html5


def replace(Klass):
    old_call = Klass.visit_reference

    def visit_reference(self, node):
        if "refuri" in node:
            refuri = node.get("refuri")
            if "generated" in refuri:
                href_anchor = refuri.split("#")
                if len(href_anchor) > 1:
                    href = href_anchor[0]
                    anchor = href_anchor[1]
                    page = href.split("/")[-1]
                    parts = page.split(".")
                    if parts[-1] == "html":
                        pagename = ".".join(parts[:-1])
                        if anchor == pagename:
                            node["refuri"] = href
        return old_call(self, node)

    Klass.visit_reference = visit_reference


replace(html.HTMLTranslator)
replace(html5.HTML5Translator)

# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_book_theme"
html_logo = "_static/compas_icon.png"
html_title = "{{ cookiecutter.project_name }}"
html_favicon = "_static/compas.ico"

html_theme_options = {
    "use_download_button": False,
    "use_repository_button": True,
    "logo": {
        "text": "{{ cookiecutter.project_name }}",
        "image_light": "_static/compas_icon.png",
        "image_dark": "_static/compas_icon_white.png",
    },
}

html_sidebars = {
    "**": [
        "navbar-logo.html",
        "sbt-sidebar-nav.html",
        "compas-sidebar-footer.html",
    ]
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "{{ cookiecutter.github_organization }}",
    "github_repo": "{{ cookiecutter.project_slug }}",
    "github_version": "main",
    "doc_path": "docs",
}

html_static_path = ["_static"]
html_css_files = ["compas.css"]
html_extra_path = []
html_last_updated_fmt = ""
html_copy_source = False
html_show_sourcelink = True
html_permalinks = False
html_permalinks_icon = ""
html_compact_lists = True
