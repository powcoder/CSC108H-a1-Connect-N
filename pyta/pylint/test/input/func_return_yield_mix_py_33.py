https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""pylint should detect yield and return mix inside generators"""
# pylint: disable=using-constant-test, inconsistent-return-statements
def somegen():
    """this is a bad generator"""
    if True:
        return 1
    else:
        yield 2

def moregen():
    """this is another bad generator"""
    if True:
        yield 1
    else:
        return 2
