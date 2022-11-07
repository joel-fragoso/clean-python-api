from .app_error import AppError


class UnauthorizedError(AppError):
    code = 401
    description = "Unauthorized"
