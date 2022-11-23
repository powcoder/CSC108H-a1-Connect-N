https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
'''
Regression test for
https://bitbucket.org/logilab/pylint/issue/128/attributeerror-when-parsing
'''
from __future__ import with_statement

def do_nothing():
    """ empty """
    with open("") as ctx.obj:  # [undefined-variable]
        context.do()  # [used-before-assignment]
        context = None
