# Standard Library
from logging import getLogger

# Current project
from calculator.fibonacci import Fibonacci

FUNCTIONS = ["fib"]


class Executor:
    def __init__(self, fibonacci: Fibonacci) -> None:
        self._log = getLogger(f"{__name__}.{self.__class__.__name__}")
        self._log.info("Creating parser")
        self._fibonacci = fibonacci

    def parse(self, func: str, value: int):
        if func == "fib":
            return self._fibonacci.calculate(value)
        raise ValueError(f"Unknown function {func}")
