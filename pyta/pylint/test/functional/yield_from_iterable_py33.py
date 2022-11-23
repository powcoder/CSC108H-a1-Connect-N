https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""
Check that `yield from`-statement takes an iterable.
"""
# pylint: disable=missing-docstring

def to_ten():
    yield from 10  # [not-an-iterable]
