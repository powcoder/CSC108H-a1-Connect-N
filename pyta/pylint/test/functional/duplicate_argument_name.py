https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Check for duplicate function arguments."""


def foo1(_, _): # [duplicate-argument-name]
    """Function with duplicate argument name."""

def foo2(_, *_): # [duplicate-argument-name]
    """Function with duplicate argument name."""

def foo3(_, _=3): # [duplicate-argument-name]
    """Function with duplicate argument name."""
