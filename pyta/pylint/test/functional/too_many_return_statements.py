https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring

def stupid_function(arg): # [too-many-return-statements]
    if arg == 1:
        return 1
    if arg == 2:
        return 2
    if arg == 3:
        return 3
    if arg == 4:
        return 4
    if arg == 5:
        return 5
    if arg == 6:
        return 6
    if arg == 7:
        return 7
    if arg == 8:
        return 8
    if arg == 9:
        return 9
    if arg == 10:
        return 10
    return None


def many_yield(text):
    """Not a problem"""
    if text:
        yield "    line 1: %s\n" % text
        yield "    line 2\n"
        yield "    line 3\n"
        yield "    line 4\n"
        yield "    line 5\n"
    else:
        yield "    line 6\n"
        yield "    line 7\n"
        yield "    line 8\n"
        yield "    line 9\n"
        yield "    line 10\n"
