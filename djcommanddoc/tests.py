import unittest
try:
    from unittest.mock import MagicMock, patch
except ImportError:
    from mock import MagicMock, patch
import djcommanddoc


class VisitDjcommandNodeTest(unittest.TestCase):
    @patch('djcommanddoc.Command', create=True)
    def test_visit_djcommand_node(self, mock_command):
        mock_translator = MagicMock()
        mock_node = MagicMock(rawsource='djcommanddoc')
        djcommanddoc.visit_djcommand_node(mock_translator,
                                          mock_node)
        self.assertEqual(3, len(mock_translator.body.append.call_args_list))


class DepartDjcommandNodeTest(unittest.TestCase):
    @patch('djcommanddoc.Command', create=True)
    def test_depart_djcommand_node(self, mock_command):
        mock_translator = MagicMock()
        mock_node = MagicMock(rawsource='djcommanddoc')
        djcommanddoc.depart_djcommand_node(mock_translator,
                                           mock_node)

if __name__ == '__main__':
    unittest.main()
