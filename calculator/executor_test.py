# Dependencies
from pytest import fixture, raises

# Current project
from calculator.executor import Executor


class TestExecutor:
    def test_wrong_function_raises_error(self, sut):
        # arrange
        # act
        # assert
        with raises(ValueError) as excinfo:
            sut.parse("unknown", 1)

        assert "Unknown function unknown" in str(excinfo.value)

    @fixture
    def sut(self):
        return Executor(None)
