# Standard Library
from logging.config import fileConfig

# Current project
from calculator.executor import Executor
from calculator.fibonacci import Fibonacci
from config import Config


class Container:
    fileConfig("log.ini")

    config = Config()
    fibonacci = Fibonacci()
    parser = Executor(fibonacci)


container = Container()
