https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Test that `yield` or `yield from` can't be used inside an async function."""
# pylint: disable=missing-docstring, unused-variable

async def good_coro():
    def _inner():
        yield 42
        yield from [1, 2, 3]


async def bad_coro():
    yield 42 # [yield-inside-async-function]
    yield from [1, 2, 3] # [yield-inside-async-function]
