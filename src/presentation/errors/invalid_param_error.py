from .app_error import AppError


class InvalidParamError(AppError):
    code = 400
    description = "Invalid param"

    # def __init__(self, param_name: str) -> None:
    #     super().__init__(f"Invalid param: {param_name}")
    #     self.name = "InvalidParamError"
