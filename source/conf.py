# Configuration file for the Sphinx documentation builder.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../src/"))
sys.path.insert(0, os.path.abspath("../src/Functions/"))


# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TSP'
copyright = '2023, Andrew Spiro'
author = 'Andrew Spiro'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.viewcode',
  'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
html_show_sourcelink = True
