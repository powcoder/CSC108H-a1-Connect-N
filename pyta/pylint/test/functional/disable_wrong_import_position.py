https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Checks that disabling 'wrong-import-position' on a statement prevents it from
invalidating subsequent imports."""
# pylint: disable=unused-import

CONSTANT = True  # pylint: disable=wrong-import-position

import sys
