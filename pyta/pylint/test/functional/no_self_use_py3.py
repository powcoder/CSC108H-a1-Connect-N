https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring,no-init,unused-argument,invalid-name,too-few-public-methods

class A:
    def __init__(self):
        self.store = {}

    def get(self, key, default=None):
        return self.store.get(key, default)

class B(A):
    def get_memo(self, obj):
        return super().get(obj)
