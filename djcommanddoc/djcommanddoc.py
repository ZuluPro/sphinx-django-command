from importlib import import_module
from docutils import nodes
from docutils.parsers.rst import Directive


class djcommand(nodes.Element):
    pass


def visit_djcommand_node_html(self, node):
    self.visit_admonition(node)
    self.body.append(self.starttag(node, "pre"))

    command_name = node.rawsource.split('.')[-1]
    command_module = import_module(node.rawsource)
    parser = command_module.Command().create_parser('manage.py', command_name)
    self.body.append(parser.format_help())

    self.body.append("</pre>")


def depart_djcommand_node_html(self, node):
    self.depart_admonition(node)


def visit_djcommand_node_latex(self, node):
    command_name = node.rawsource.split('.')[-1]
    command_module = import_module(node.rawsource)
    parser = command_module.Command().create_parser('manage.py', command_name)
    self.body.append(parser.format_help())


def depart_djcommand_node_latex(self, node):
    pass


class DjCommandDirective(Directive):
    has_content = True
    node_class = djcommand

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = self.node_class(text)
        return [node]
