https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
""" Testing with statements that use generators. This should not crash. """
# pylint: disable=useless-object-inheritance

class Base(object):
    """ Base class. """
    val = 0

    def gen(self):
        """ A generator. """
        yield self.val

    def fun(self):
        """ With statement using a generator. """
        with self.gen():  # [not-context-manager]
            pass
