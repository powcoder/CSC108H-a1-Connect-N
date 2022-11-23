https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Tests for inconsistent-mro."""
# pylint: disable=missing-docstring,too-few-public-methods,no-init

class Str(str):
    pass


class Inconsistent(str, Str): # [inconsistent-mro]
    pass
