# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from sphinx.builders.html import StandaloneHTMLBuilder
import subprocess, os

# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'
if read_the_docs_build:
    subprocess.call("cd .. ; doxygen", shell=True)

project = 'CPUDebugger'
copyright = '2023, David Li'
author = 'David Li'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    # 'sphinx_sitemap',
    'sphinx.ext.inheritance_diagram',
    'breathe',
    'exhale'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']
exclude_patterns = ['Read the Docs', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url'             : '',
    'analytics_id'              : '',  # Provided by Google in your dashboard
    'display_version'           : True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links'      : False,

    'logo_only'                 : False,

    # Toc options
    'collapse_navigation'       : True,
    'sticky_navigation'         : True,
    'navigation_depth'          : 4,
    'includehidden'             : True,
    'titles_only'               : False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

html_logo = '../icon.svg'
github_url = 'https://github.com/sustech-cs304/team-project-2339'

# -- Breathe configuration -------------------------------------------------

breathe_projects = {
    "CPUDebugger": "../../documentations/Developer Manual/Doxygen/xml/"
}
breathe_projects_source = {
    "CPUDebugger": ("../..", [])
}
breathe_default_project = "CPUDebugger"
# breathe_default_members = ('members', 'undoc-members')

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder"   : "./api",
    "rootFileName"        : "library_root.rst",
    "rootFileTitle"       : "Library API",
    "doxygenStripFromPath": "../..",
    # Suggested optional arguments
    "createTreeView"      : True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'
