https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Test that a name is both nonlocal and global in the same scope."""
# pylint: disable=missing-docstring,global-variable-not-assigned,invalid-name,nonlocal-without-binding

def bad(): # [nonlocal-and-global]
    nonlocal missing
    global missing

def good():
    nonlocal missing
    def test():
        global missing
    return test
