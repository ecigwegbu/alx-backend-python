from unittest.mock import patch, Mock, PropertyMock
import unittest

class MyClass:
    @property
    def last_transaction(self):
        # an expensive and complicated DB query here
        pass

class testProperty(unittest.TestCase):
    """Test"""
    def test(self):

        myclass = MyClass()

        with patch('__main__.MyClass.last_transaction', new_callable=PropertyMock) as mock_last_transaction:
            mock_last_transaction.return_value = "Hello"  # Transaction()
            print(myclass.last_transaction)
            mock_last_transaction.assert_called_once_with()
