import os
import sys
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('../..'))  # Ajout du chemin du projet pour accéder aux modules

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python OC Lettings'
copyright = '2024, Heric'
author = 'Heric'
release = '0.0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Pour générer la documentation à partir des docstrings
    'sphinx.ext.viewcode',  # Pour générer des liens vers le code source
    'sphinx.ext.napoleon',  # Pour gérer les docstrings Google et Numpy
    'sphinx_rtd_theme',  # Pour utiliser le thème Read the Docs
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
