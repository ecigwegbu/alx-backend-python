class Calculator:
    def __init__(self, a: int, b: int) -> None:
        self._a = a
        self._b = b
        self._data = None

    @property
    def data(self) -> int:
        if self._data is None:
            # Simulating some computation based on attributes 'a' and 'b'
            self._data = self._a + self._b
        return self._data

    @property
    def result(self) -> int:
        # Accessing the 'data' property to perform additional computation
        return self.data + 50

import unittest
from unittest.mock import patch

class TestCalculateSum(unittest.TestCase):
    def test_calculate_sum_with_mocked_properties(self):
        # Create a Calculator instance
        calculator = Calculator(5, 10)

        # Mock the 'data' property of the Calculator instance
        with patch.object(calculator, 'data', return_value=50) as mock_data:
            # Mock the 'result' property, which depends on the 'data' property
            with patch.object(calculator, 'result', return_value=100) as mock_result:
                # Access the 'result' property, which depends on the mocked 'data' property
                result: int = calculator.result

                # Assert the result
                self.assertEqual(result, 100)

        # The mock 'data' property should have been called once with the mocked value
        mock_data.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
