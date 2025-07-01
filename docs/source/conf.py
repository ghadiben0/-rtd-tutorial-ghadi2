# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Welcome to MES Doc hub!'
copyright = '2025, Powered by Karim Atigi & Ghada Ben Nasser'
author = 'Ghada Ben Nasser'

release = '0.1'
version = 'Release Version 0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    extensions += ['hoverxref.extension']
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False # This removes the "View page source" link

html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    "show_toc_level": 2,  # or higher depending on your needs
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

templates_path = ['_templates']


