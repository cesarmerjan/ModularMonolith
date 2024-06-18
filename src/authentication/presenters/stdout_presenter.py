from src.authentication.views.stdout_view import StdoutView


class StdoutPresenter:
    def render(self, data: dict, response_type: str) -> None:
        StdoutView.render(data, response_type)
