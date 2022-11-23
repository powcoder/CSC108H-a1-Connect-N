https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Tests for redefining builtins."""
from __future__ import print_function

def function():
    """Redefined local."""
    type = 1  # [redefined-builtin]
    print(type)

# pylint:disable=invalid-name
map = {}  # [redefined-builtin]
__doc__ = 'reset the doc'
