https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Test that `if` in formatted string literal won't break Pylint."""
# pylint: disable=missing-docstring, pointless-statement, using-constant-test

f'{"+" if True else "-"}'
if True:
    pass
elif True:
    pass
