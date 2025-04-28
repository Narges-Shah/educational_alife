
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Educational ALife Ecosystem'
copyright = '2025'
author = 'Narges Shahhoseini'

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
