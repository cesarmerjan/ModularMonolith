import click

from src.authentication.cli import users
from src.authentication.cli.context import CliContext
from src.contexts import DatabaseContext


@click.group()
@click.pass_context
def cli(context: CliContext):
    context.ensure_object(DatabaseContext)
    pass


users.register_on(cli)
