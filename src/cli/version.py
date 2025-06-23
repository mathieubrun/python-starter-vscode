from typer import Typer

app = Typer()


@app.command()
def version():
    print("My CLI Version 1.0")
