import sys


class StdoutView:
    SUCCESS = "\033[92m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    END = "\033[0m"

    RESPONSE_TYPES: dict = {
        "success": SUCCESS,
        "warning": WARNING,
        "error": ERROR,
    }

    @classmethod
    def render(cls, data: dict, response_type: str):
        color = cls.RESPONSE_TYPES[response_type]
        for key, value in data.items():
            message = f"{color}{key}: {value}{cls.END}\n"
            sys.stdout.write(message)
