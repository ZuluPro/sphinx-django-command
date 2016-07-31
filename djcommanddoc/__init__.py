#!/user/bin/env python
"""Sphinx plugin for help Django commands documentation."""
VERSION = (0, 1, 3)
__version__ = '.'.join([str(i) for i in VERSION])
__author__ = 'Anthony Monthe (ZuluPro)'
__email__ = 'anthony.monthe@gmail.com'
__url__ = 'https://github.com/ZuluPro/sphinx-django-command'


def setup(app):
    from .djcommanddoc import (DjCommandDirective, djcommand,
                               visit_djcommand_node_html,
                               depart_djcommand_node_html,
                               visit_djcommand_node_latex,
                               depart_djcommand_node_latex)
    app.add_node(djcommand,
                 html=(visit_djcommand_node_html, depart_djcommand_node_html),
                 latex=(visit_djcommand_node_latex, depart_djcommand_node_latex))
    app.add_directive('djcommand', DjCommandDirective)
    return {'version': __version__}
