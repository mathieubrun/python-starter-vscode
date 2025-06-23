from typer import Typer
from .suffix import app as suffix_app
from .version import app as version_app


app = Typer()

app.add_typer(version_app)
app.add_typer(suffix_app)
