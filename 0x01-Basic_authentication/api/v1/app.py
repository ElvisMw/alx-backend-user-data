#!/usr/bin/env python3
"""
This script starts the Flask application and initializes the necessary
components for the API.
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

app = Flask(__name__)
""" Flask application instance """

app.register_blueprint(app_views)
""" Register the views blueprint """

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
""" Enable CORS for all routes under /api/v1 """

auth = None
""" Instance of the authentication class """

AUTH_TYPE = getenv("AUTH_TYPE")
""" Authentication type (basic_auth or auth) """

if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
    """ Initialize the Auth class if authentication type is auth """
elif AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
    """ Initialize the BasicAuth class if authentication type is basic_auth """


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Error handler for 404 Not Found errors.
    Returns a JSON response with an error message.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
    Error handler for 401 Unauthorized errors.
    Returns a JSON response with an error message.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """
    Error handler for 403 Forbidden errors.
    Returns a JSON response with an error message.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request() -> str:
    """
    Before request handler.
    Authenticates the request if authentication is enabled.
    """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
