https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""test cyclic import
"""
# pylint: disable=no-absolute-import
from __future__ import print_function

from . import w0401_cycle  # pylint: disable=cyclic-import

if w0401_cycle:
    print(w0401_cycle)
