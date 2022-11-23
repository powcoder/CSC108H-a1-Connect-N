https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring

# pylint: disable=unused-import, undefined-variable; false positives :-(

import functools


@functools.lru_cache()
def func():
    pass


func.cache_clear()
