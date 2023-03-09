# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../lsdo_project_template/core')) # for autodoc
# sys.path.insert(0, os.path.abspath('../examples'))


# -- Project information -----------------------------------------------------

project = 'lsdo_project_template'
copyright = '2022, anugrah'
author = 'anugrah'
version = '0.1'
# release = 0.1.0rtc


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ["sphinx.ext.autodoc"]
extensions = [
    "sphinx_rtd_theme",
    "autoapi.extension", # autoapi is not needed when using autodoc
    # "sphinx.ext.autodoc",
    # "sphinx.ext.napoleon", # another extension to read numpydoc style but 'numpydoc' extension looks better
    "numpydoc", # numpydoc already includes autodoc
    # "myst_parser", # compiles .md, .myst files
    "myst_nb", # compiles .md, .myst, .ipynb files
    "sphinx.ext.viewcode", # adds the source code for classes and functions in auto generated api ref
    "sphinxcontrib.collections", # adds files from outside src and executes functions before Sphinx builds
]
autoapi_dirs = ["../../lsdo_project_template/core"]

# root_doc = 'index'
root_doc = 'welcome'

# source_suffix = {
#     '.rst': 'restructuredtext',
#     # '.md': 'markdown',
#     # '.ipynb': 'Jupyter notebook',
#     }

# # source_parsers = {'.md': 'myst_nb',
# #                 '.ipynb': 'myst_nb',
# #                 }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'welcome.md']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'classic'
# html_theme = 'sphinxdoc'
# html_theme = 'nature'
# html_theme = 'bizstyle'
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # 'style_nav_header_background': 'white',
    # Toc options
    # 'collapse_navigation': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    # 'titles_only': False
    'titles_only': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# extensions = [
#     "myst_nb",
#     "autoapi.extension",
#     "sphinx.ext.napoleon",
#     "sphinx.ext.viewcode",
# ]
# autoapi_dirs = ["../src"]

import sys
# import os

# import nbformat
# from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

# nb = new_notebook()
# with open(sys.argv[1]) as f:
#     code = f.read()

# ex_name = sys.argv[1][3:-3]
# nb.cells.append(new_markdown_cell('# '+ ex_name))
# nb.cells.append(new_code_cell(code))
# nbformat.write(nb, sys.argv[1][:-3]+'.ipynb')

import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

def py2nb(config):
    examples = [filename for filename in os.listdir(config['from']) if filename.startswith("ex_")]
    # os.mkdir(config['target']+'\examples') # This mkdir is necessary since
    for ex in examples:
        nb = new_notebook()
        with open(config['from']+ex) as f:
            code = f.read()

        ex_name = ex[3:-3]
        nb.cells.append(new_markdown_cell('# '+ ex_name))
        nb.cells.append(new_code_cell(code))
        nbformat.write(nb, config['target']+ex[:-3]+'.ipynb')

    return



collections = {
   'copy_tutorials': {
      'driver': 'copy_folder',
      'source': '../examples/tutorials', # source relative to path of makefile, not wrt /src
      'target': 'tutorials/',
      'ignore': [],
    #   'active': True,
      'clean': True,
      'final_clean': True,
   },

    'convert_examples': {
      'driver': 'writer_function',  # uses custom WriterFunctionDriver written by Anugrah
      'from'  : '../examples/',     # source relative to path of makefile, not wrt /src
      'source': py2nb,             # custom function written above in `conf.py`
      'target': 'examples/',       # target was a file for original FunctionDriver, e.g., 'target': 'examples/temp.txt'
    #   'active': True,            # the original FunctionDriver was supposed to write only 1 file.
      'clean': True,
      'final_clean': True,
    #   'write_result': True,      # this prevents original FunctionDriver from writing to the target file
   },
}
