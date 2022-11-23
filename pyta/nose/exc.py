https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Exceptions for marking tests as skipped or deprecated.

This module exists to provide backwards compatibility with previous
versions of nose where skipped and deprecated tests were core
functionality, rather than being provided by plugins. It may be
removed in a future release.
"""
from nose.plugins.skip import SkipTest
from nose.plugins.deprecated import DeprecatedTest
