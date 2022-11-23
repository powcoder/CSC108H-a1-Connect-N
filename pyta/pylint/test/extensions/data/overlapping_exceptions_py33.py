https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring

import socket

try:
    pass
except (IOError, OSError): # [overlapping-except]
    pass

try:
    pass
except (socket.error, OSError): # [overlapping-except]
    pass

try:
    pass
except (ConnectionError, socket.error): # [overlapping-except]
    pass
