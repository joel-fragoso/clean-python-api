from flask import jsonify, request

from src.presentation.protocols import Controller


def adapt_route(controller: Controller):
    def adapt_route_func():
        http_request = request.get_json()
        http_response = controller.handle(http_request)
        if http_response.code >= 200 and http_response.code <= 299:
            return jsonify(http_response.body), http_response.code
        else:
            return (
                jsonify({"error": http_response.body.to_dict()}),
                http_response.code,
            )

    return adapt_route_func
