https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
""" Functional tests for method deprecation. """
# pylint: disable=no-value-for-parameter
import unittest
from importlib.machinery import SourceFileLoader, SourcelessFileLoader

SourceFileLoader('unittest', unittest.__file__).load_module() # [deprecated-method]
SourcelessFileLoader('unittest', unittest.__file__).load_module() # [deprecated-method]
