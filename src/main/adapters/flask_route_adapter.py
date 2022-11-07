from flask import json, jsonify, request

from src.presentation.protocols import Controller


def adapt_route(controller: Controller):
    def adapt_route_func():
        http_request: dict = {}
        if request.json is not None:
            http_request = {**request.json}
        if request.args is not None:
            http_request = {**request.args}
        http_response = controller.handle(http_request)
        if http_response.code >= 200 and http_response.code <= 299:
            return jsonify(json.dumps(http_response.body)), http_response.code
        else:
            return (
                jsonify(json.dumps({"error": http_response.body.message})),
                http_response.code,
            )

    return adapt_route_func
