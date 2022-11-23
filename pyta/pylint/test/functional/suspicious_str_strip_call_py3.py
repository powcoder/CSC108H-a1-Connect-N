https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""Suspicious str.strip calls."""
__revision__ = 1

''.strip('yo')
''.strip()

u''.strip('http://')  # [bad-str-strip-call]
u''.lstrip('http://')  # [bad-str-strip-call]
b''.rstrip('http://')  # [bad-str-strip-call]
