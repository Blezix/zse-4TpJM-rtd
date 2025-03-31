# conf.py - Konfiguracja Sphinx dla Read the Docs
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Nazwa Projektu'
copyright = '2025, Twoje Imię'
author = 'Twoje Imię'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser'  # Obsługa Markdown
]

html_theme = 'sphinx_rtd_theme'



