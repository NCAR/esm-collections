# -*- coding: utf-8 -*-


import datetime

import esm_collections

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'myst_nb',
    'sphinxext.opengraph',
    'sphinx_copybutton',
    'sphinx_comments',
    'sphinxcontrib.autodoc_pydantic',
    'sphinx_inline_tabs',
]

autodoc_member_order = 'groupwise'

# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image']
myst_url_schemes = ['http', 'https', 'mailto']

# sphinx-copybutton configurations
copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = []
autodoc_typehints = 'none'

# Napoleon configurations

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = False

autodoc_pydantic_model_show_json = True
autodoc_pydantic_settings_show_json = False

jupyter_execute_notebooks = 'cache'
execution_timeout = 600
execution_allow_errors = True


# The master toctree document.
master_doc = 'index'

# General information about the project.
current_year = datetime.datetime.now().year
project = u'esm_collections'
copyright = f'2021-{current_year}, esm_collections developers'
author = u'esm_collections developers'


# The short X.Y version.
version = esm_collections.__version__.split('+')[0]
# The full version, including alpha/beta/rc tags.
release = esm_collections.__version__


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'
html_title = ''

html_context = {
    'github_user': 'NCAR',
    'github_repo': 'esm-collections',
    'github_version': 'main',
    'doc_path': 'docs',
}
html_theme_options = dict(
    # analytics_id=''  this is configured in rtfd.io
    # canonical_url="",
)


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = '../_static/images/NSF_4-Color_bitmap_Logo.png'


# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'


# Output file base name for HTML help builder.
htmlhelp_basename = 'esm_collections_doc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}


latex_documents = [('index', 'esm_collections.tex', u'esm-collections Documentation', author, 'manual')]

man_pages = [('index', 'esm-collections', u'esm-collections Documentation', [author], 1)]

texinfo_documents = [
    (
        'index',
        'esm-collections',
        u'esm-collections Documentation',
        author,
        'esm-collections',
        'One line description of project.',
        'Miscellaneous',
    )
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'xarray': ('http://xarray.pydata.org/en/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'fsspec': ('https://filesystem-spec.readthedocs.io/en/latest/', None),
}