# Dependencies
from fibonacci import Fibonacci
from pytest import fixture, raises


class TestFibonacci:
    def test_one_is_one(self, sut):
        # arrange
        # act
        result = sut.calculate(1)

        # assert
        assert result == 1

    def test_two_is_one(self, sut):
        # arrange
        # act
        result = sut.calculate(2)

        # assert
        assert result == 1

    def test_minus_one_raises_error(self, sut):
        # arrange
        # act
        # assert
        with raises(ValueError) as excinfo:
            sut.calculate(-1)

        assert "not a positive integer" in str(excinfo.value)

    @fixture
    def sut(self):
        return Fibonacci()
