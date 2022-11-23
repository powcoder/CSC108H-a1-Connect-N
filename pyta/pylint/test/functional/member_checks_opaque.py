https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring,import-error

from unknown import Unknown, some_value


def test(argument):
    if argument:
        return 42
    return Unknown


test(some_value).test() # [no-member]
