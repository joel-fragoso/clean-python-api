from .app_error import AppError


class ServerError(AppError):
    code = 500
    description = "Internal server error"
