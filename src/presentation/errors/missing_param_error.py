from .app_error import AppError


class MissingParamError(AppError):
    code = 400
    description = "Missing param"

    # def __init__(self, param_name: str) -> None:
    #     super().__init__(f"Missing param: {param_name}")
    #     self.name = "MissingParamError"
