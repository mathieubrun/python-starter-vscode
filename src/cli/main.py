from dishka import Scope
from typer import Context, Typer

from cli.users_command import users_app
from core import create_dishka_container

app = Typer()

app_container = create_dishka_container(Scope.APP)

app.add_typer(users_app, name="users")


@app.callback()
def main(ctx: Context):
    ctx.obj = app_container
    ctx.call_on_close(app_container.close)


@app.command()
def version():
    print("My CLI Version 0.0.0")
    print("My CLI Version 0.0.0")
