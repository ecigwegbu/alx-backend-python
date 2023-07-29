from unittest.mock import patch, Mock, PropertyMock
import unittest

class Foo:
    @property
    def foo(self):
        return 'something'
    @foo.setter
    def foo(self, value):
        pass

with patch('Foo.foo', new_callable=PropertyMock) as mock_foo:
    mock_foo.return_value = 'mockity-mock'
    this_foo = Foo()
    print(this_foo.foo)
    this_foo.foo = 6

# mockity-mock
mock_foo.mock_calls
