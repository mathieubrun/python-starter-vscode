# Dependencies
from pydantic import BaseSettings


class Config(BaseSettings):
    debug: bool = True
