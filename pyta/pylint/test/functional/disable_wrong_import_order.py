https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Checks that disabling 'wrong-import-order' on an import prevents subsequent
imports from being considered out-of-order in respect to it but does not prevent
it from being considered for 'ungrouped-imports'."""
# pylint: disable=unused-import,import-error,no-name-in-module

from first_party.foo import bar # pylint: disable=wrong-import-order
import logging
import os.path
import sys
from astroid import are_exclusive
import first_party  # [ungrouped-imports]
