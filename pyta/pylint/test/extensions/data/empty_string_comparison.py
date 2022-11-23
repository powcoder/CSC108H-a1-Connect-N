https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=literal-comparison,missing-docstring

X = ''
Y = 'test'

if X is '':  # [compare-to-empty-string]
    pass

if Y is not "":  # [compare-to-empty-string]
    pass

if X == "":  # [compare-to-empty-string]
    pass

if Y != '':  # [compare-to-empty-string]
    pass
