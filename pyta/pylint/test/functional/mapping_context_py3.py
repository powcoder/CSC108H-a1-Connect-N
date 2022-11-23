https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods,no-self-use
from __future__ import print_function

def test(**kwargs):
    print(kwargs)

# metaclasses as mappings
class Meta(type):
    def __getitem__(cls, key):
        return ord(key)

    def keys(cls):
        return ['a', 'b', 'c']

class SomeClass(metaclass=Meta):
    pass

test(**SomeClass)
test(**SomeClass())  # [not-a-mapping]
