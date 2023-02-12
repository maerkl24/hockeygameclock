# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import pathlib

# Set repository base path
repository_path = pathlib.Path(__file__).resolve().parent.parent

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "hockeygameclock"
copyright = "2023, Kilian Märkl"
author = "Kilian Märkl"
release = "1.0.0"


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


# -- Options for furo theme --------------------------------------------------
# https://pradyunsg.me/furo/customisation/logo/
# https://pradyunsg.me/furo/customisation/edit-button/

html_theme_options = {
    "light_logo": "logo.png",
    "dark_logo": "logo.png",
    "source_repository": "https://github.com/maerkl24/hockeygameclock/",
    "source_branch": "main",
    "source_directory": "doc/",
    "sidebar_hide_name": True,
}


# -- Options for sphinxcontrib.plantuml --------------------------------------
# https://github.com/sphinx-contrib/plantuml/

plantuml = f"java -jar {repository_path}/tools/plantuml.jar"
