from typing import Annotated

from typer import Argument, Context, Option, Typer

from core.config import SecondaryService

users_app = Typer()


@users_app.command()
def list(ctx: Context):
    print(ctx.obj.get(SecondaryService).get_all())


@users_app.command()
def add(
    ctx: Context,
    name: Annotated[str, Argument(help="The user name.")],
    email: Annotated[str, Option("--email", "-e", help="The user email.")],
):
    print(ctx.obj.get(SecondaryService).add_user(name, email))
