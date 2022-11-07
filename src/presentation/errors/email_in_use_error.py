from .app_error import AppError


class EmailInUseError(AppError):
    code = 400
    description = "The received email is already in use"
