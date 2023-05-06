# Standard Library
from logging import getLogger


class Fibonacci:
    cache: list[int]

    def __init__(self):
        self.log = getLogger(f"{__name__}.{self.__class__.__name__}")
        self.log.info("Creating fibonnaci calculator")
        self.cache = [0, 1]

    def calculate(self, n: int) -> int:
        if n < 0:
            raise ValueError(f"{n} is not a positive integer")

        if n < len(self.cache):
            self.log.debug(f"Fibonacci value is in cache for {n}")
            return self.cache[n]

        self.log.info(f"Computing fibonacci for {n}")
        res = self.calculate(n - 1) + self.calculate(n - 2)
        self.cache.append(res)
        return res
