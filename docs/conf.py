# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import pathlib
import hockeygameclock

# Set repository base path
REPOSITORY_PATH = pathlib.Path(__file__).resolve().parent.parent


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Hockey Game Clock"
copyright = "2023, Kilian Märkl"
author = "Kilian Märkl"
release = hockeygameclock.__version__


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.plantuml",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_favicon = "_static/favicon.ico"
html_title = f"{project} {release}"


# -- Options for furo theme --------------------------------------------------
# https://pradyunsg.me/furo/customisation/logo/
# https://pradyunsg.me/furo/customisation/edit-button/

html_theme_options = {
    "light_logo": "logo.png",
    "dark_logo": "logo.png",
    "source_repository": "https://github.com/maerkl24/hockeygameclock/",
    "source_branch": "main",
    "source_directory": "docs/",
    "sidebar_hide_name": False,
}


# -- Options for sphinxcontrib.plantuml --------------------------------------
# https://github.com/sphinx-contrib/plantuml/

plantuml = f"java -jar {REPOSITORY_PATH.as_posix()}/tools/plantuml.jar"
