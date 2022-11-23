https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring,unused-import
try:
    import urllib2 as urllib_request #@
    import urllib2 as urllib_error
    from urlparse import urlparse
except ImportError:
    # python2
    from urllib import request as urllib_request
    from urllib import error as urllib_error
    from urllib.parse import urlparseq
