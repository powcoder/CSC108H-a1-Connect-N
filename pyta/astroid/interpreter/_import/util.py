https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# Copyright (c) 2016, 2018 Claudiu Popa <pcmanticore@gmail.com>

try:
    import pkg_resources
except ImportError:
    pkg_resources = None


def is_namespace(modname):
    return (pkg_resources is not None
            and modname in pkg_resources._namespace_packages)
