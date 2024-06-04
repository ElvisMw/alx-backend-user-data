#!/usr/bin/env python3
""" Module of Index views """
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ GET /api/v1/status - Returns the status of the API """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats():
    """ GET /api/v1/stats - Returns the number of each objects """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden_endpoint():
    """ GET /api/v1/forbidden - Raises a 403 error """
    abort(403)
