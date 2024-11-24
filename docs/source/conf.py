# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Руководство пользователя'
copyright = '2024, CodeBIM.ru'
author = 'Eugene Kiryan'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static', '_static/css/custom.css']

html_show_sourcelink = False

html_theme_options = {
    'logo': 'CodeBIM_Logo.png',
    'logo_name': True,
    'logo_text_align': 'center',
    'font_family': 'Segoe UI',
    'code_font_family': 'Cascadia Code',
    'link_hover': 'turquoise',
    'sidebar_link_underscore': 'turquoise',
    'sidebar_width':  '17rem',
    'page_width':  '83rem'
}
