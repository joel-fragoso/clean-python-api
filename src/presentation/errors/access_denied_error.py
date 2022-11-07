from .app_error import AppError


class AccessDeniedError(AppError):
    code = 403
    description = "Access denied"
