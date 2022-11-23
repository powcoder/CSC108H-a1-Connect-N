https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Test that non-inferable __all__ variables do not make Pylint crash."""

__all__ = sorted([
    'Dummy',
    'NonExistant',
    'path',
    'func',
    'inner',
    'InnerKlass'])
