https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring

exec('a = __revision__') # [exec-used]
exec('a = 1', globals={}) # [exec-used]

exec('a = 1', globals=globals()) # [exec-used]

def func():
    exec('b = 1') # [exec-used]
