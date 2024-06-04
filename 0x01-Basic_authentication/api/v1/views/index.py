#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, Response
from api.v1.views import app_views
from typing import Dict
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> Response:
    """
    GET /api/v1/status
    Returns the status of the API.

    Return:
        - JSON response with the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> Response:
    """
    GET /api/v1/stats
    Returns the number of each object.

    Return:
        - JSON response with the count of User objects
    """
    stats: Dict[str, int] = {}
    stats['users'] = User.count()
    return jsonify(stats)
