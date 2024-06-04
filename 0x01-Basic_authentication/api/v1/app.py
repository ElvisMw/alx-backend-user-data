#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, Response
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error) -> Response:
    """
    Not found handler.

    Parameters:
        error (Exception): The exception object representing the not
        found error

    Returns:
        Response: A JSON response indicating that the resource was not found
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> Response:
    """
    Handle unauthorized requests by returning a JSON response
    with an "error" key set to "Unauthorized" and a status code of 401.

    Parameters:
        error (Exception): The exception object representing the
        unauthorized request.

    Returns:
        Response: A JSON response and the status code.
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
