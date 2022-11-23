https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""
Test that pylint doesn't crash when a relative import
depends on the local __init__, which contains an expected syntax error.
"""
from . import missing
