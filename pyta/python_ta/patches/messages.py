https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Patch pylint message-handling behaviour."""
from pylint.utils import MessagesHandlerMixIn, UNDEFINED
from pylint.lint import PyLinter
from astroid.transforms import TransformVisitor
from python_ta.transforms.setendings import register_transforms


def patch_messages():
    """Patch MessagesHandlerMixIn to pass the node to reporter."""
    old_add_message = MessagesHandlerMixIn.add_message

    def new_add_message(self, msg_id, line=None, node=None, args=None,
                        confidence=UNDEFINED, col_offset=None):
        old_add_message(self, msg_id, line, node, args, confidence, col_offset)
        msg_info = self.msgs_store.get_message_definition(msg_id)
        self.reporter.handle_node(msg_info, node)

    MessagesHandlerMixIn.add_message = new_add_message


def patch_linter_transform():
    """Patch PyLinter class to apply message transform with source code."""
    old_get_ast = PyLinter.get_ast

    def new_get_ast(self, filepath, modname):
        ast = old_get_ast(self, filepath, modname)
        if ast is not None:
            with open(filepath, encoding='utf-8') as f:
                source_code = f.readlines()
            ending_transformer = TransformVisitor()
            register_transforms(source_code, ending_transformer)
            ending_transformer.visit(ast)
        return ast

    PyLinter.get_ast = new_get_ast
