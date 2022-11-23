https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""
Check that instantiating a class with `abc.ABCMeta` as ancestor fails if it
defines abstract methods.
"""

# pylint: disable=too-few-public-methods, missing-docstring, no-init

import abc



class BadClass(abc.ABC):
    @abc.abstractmethod
    def test(self):
        pass

def main():
    """ do nothing """
    BadClass() # [abstract-class-instantiated]
