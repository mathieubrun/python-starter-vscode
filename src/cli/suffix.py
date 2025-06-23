from business import get_value
from typer import Typer

app = Typer()


@app.command()
def suffix(suffix: str):
    print(get_value(__name__) + suffix)
