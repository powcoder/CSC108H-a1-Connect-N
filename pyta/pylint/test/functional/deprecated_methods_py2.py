https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
""" Functional test for deprecated methods in Python 2 """
# pylint: disable=no-member
import os
import xml.etree.ElementTree

os.popen2('')     # [deprecated-method]
os.popen3('')     # [deprecated-method]
os.popen4('')     # [deprecated-method]
xml.etree.ElementTree.Element('elem').getchildren()     # [deprecated-method]
