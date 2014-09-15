# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import os
import sys

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('_themes'))

# sys.path.append(os.path.abspath('../tests'))
sys.path.append(os.path.abspath('../newco'))
for path in sys.path: print(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

project = "Newco"
copyright = "2014, Vinit Kumar"
version = release = "1.0.0"
language = 'English'

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.intersphinx',
	'sphinx.ext.viewcode',
	'sphinx.ext.coverage'
]
intersphinx_mapping = {
	'python': ('http://docs.python.org/2.7', None),
	'django': ('https://docs.djangoproject.com/en/1.7', 'https://docs.djangoproject.com/en/1.7/_objects'),
}
templates_path = ['_templates']
exclude_patterns = ['_build']
html_theme_path = ['_themes']
html_static_path = ['_static']
source_suffix = '.rst'
master_doc = 'index'

add_function_parentheses = True
add_module_names = True
pygments_style = 'sphinx'

htmlhelp_basename = 'newco_docs'
html_title = "Newco {version} Documentation".format(version=version)
html_short_title = "Newco"
html_last_updated_fmt = ''
html_show_sphinx = False

if os.environ.get('READTHEDOCS', None) == 'True':
	html_theme = 'default'

else:
	html_theme = 'flask'
	html_theme_options = {
		'index_logo': '',
		'index_logo_height': '0px',
	}
