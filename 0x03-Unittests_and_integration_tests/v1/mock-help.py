class unittest.mock.PropertyMock(*args, **kwargs)
A mock intended to be used as a property, or other descriptor, on a class. PropertyMock provides __get__() and __set__() methods so you can specify a return value when it is fetched.

Fetching a PropertyMock instance from an object calls the mock, with no args. Setting it calls the mock with the value being set.

>>>
class Foo:
    @property
    def foo(self):
        return 'something'
    @foo.setter
    def foo(self, value):
        pass

with patch('__main__.Foo.foo', new_callable=PropertyMock) as mock_foo:
    mock_foo.return_value = 'mockity-mock'
    this_foo = Foo()
    print(this_foo.foo)
    this_foo.foo = 6

mockity-mock
mock_foo.mock_calls
[call(), call(6)]
Because of the way mock attributes are stored you can’t directly attach a PropertyMock to a mock object. Instead you can attach it to the mock type object:

>>>
m = MagicMock()
p = PropertyMock(return_value=3)
type(m).foo = p
m.foo
3
p.assert_called_once_with()
