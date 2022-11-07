import typing as t
from flask import jsonify, request

from src.presentation.protocols import Controller


def adapt_route(controller: Controller):
    def adapt_route_func(id: t.Optional[str] = None):
        http_request = dict(
            request.get_json() or {}, **request.args or {}, **{"id": id}
        )
        http_response = controller.handle(http_request)
        if http_response.code >= 200 and http_response.code <= 299:
            return jsonify(http_response.body), http_response.code
        else:
            return (
                jsonify({"error": http_response.body.description}),
                http_response.code,
            )

    return adapt_route_func
