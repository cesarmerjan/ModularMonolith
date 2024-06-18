import click
from click.core import Group

from src.authentication.cli.context import CliContext
from src.authentication.controllers.users_controller import UsersController
from src.authentication.presenters.stdout_presenter import StdoutPresenter


@click.command("create")
@click.argument("name", type=str)
@click.argument("email", type=str)
@click.argument("password", type=str)
@click.pass_context
def create(context: CliContext, name: str, email: str, password: str):
    controller = UsersController(context.obj, StdoutPresenter())
    controller.create_user(name, email, password)


@click.command("get")
@click.argument("_uuid", type=str)
@click.pass_context
def get(context: CliContext, _uuid: str):
    controller = UsersController(context.obj, StdoutPresenter())
    controller.get_user_by_uuid(_uuid)


def register_on(cli: Group):
    @cli.group(name="users")
    @click.pass_context
    def users(context: CliContext):
        pass

    users.add_command(get)
    users.add_command(create)
