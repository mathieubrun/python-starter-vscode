# Standard Library
from unittest.mock import Mock

# Dependencies
from pytest import fixture, raises

# Current project
from calculator.executor import Executor
from calculator.fibonacci import Fibonacci


class TestExecutor:
    def test_wrong_function_raises_error(self, sut: Executor):
        # arrange
        # act
        with raises(ValueError) as excinfo:
            sut.parse("unknown", 1)

        # assert
        assert "Unknown function unknown" in str(excinfo.value)

    def test_fib_function_calls_calculate(self, sut: Executor, fibonacci: Fibonacci):
        # arrange
        given = 1
        expected = 10
        fibonacci.calculate.return_value = expected

        # act
        result = sut.parse("fib", given)

        # assert
        assert expected == result
        fibonacci.calculate.assert_called_with(given)

    @fixture
    def sut(self, fibonacci: Fibonacci) -> Executor:
        return Executor(fibonacci)

    @fixture
    def fibonacci(self) -> Fibonacci:
        return Mock()
