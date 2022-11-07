from flask import jsonify, make_response, request

from src.presentation.protocols import Middleware


def adapt_middleware(middleware: Middleware):
    def adap_middleware_func():
        http_request = {
            "access_token": request.headers["x-access-token"],
            **request.headers,
        }
        http_response = middleware.handle(http_request)
        response = make_response()
        if http_response.code == 200:
            {**request.json, **http_response.body}
            return response
        else:
            return jsonify(error=http_response.body), http_response.code

    return adap_middleware_func
