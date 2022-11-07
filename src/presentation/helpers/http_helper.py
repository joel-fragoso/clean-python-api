from traceback import format_exc
from typing import Any

from src.presentation.errors import ServerError, UnauthorizedError
from src.presentation.protocols import HttpResponse


def ok(data: Any) -> HttpResponse:
    return HttpResponse(200, data)


def no_content() -> HttpResponse:
    return HttpResponse(204, None)


def bad_request(error: Exception) -> HttpResponse:
    return HttpResponse(400, error)


def unauthorized() -> HttpResponse:
    return HttpResponse(401, UnauthorizedError())


def forbidden(error: Exception) -> HttpResponse:
    return HttpResponse(403, error)


def server_error(error: Exception) -> HttpResponse:
    return HttpResponse(500, ServerError(format_exc()))
