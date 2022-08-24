# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'hockeyclock'
copyright = '2022, Kilian Märkl'
author = 'Kilian Märkl'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# -- Options for furo theme --------------------------------------------------
# https://pradyunsg.me/furo/customisation/logo/
# https://pradyunsg.me/furo/customisation/edit-button/
html_theme_options = {
    'light_logo': 'logo.png',
    'dark_logo': 'logo.png',
    'source_repository': 'https://github.com/maerkl24/hockeyclock/',
    'source_branch': 'main',
    'source_directory': 'docs/',
}