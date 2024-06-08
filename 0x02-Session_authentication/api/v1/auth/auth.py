#!/usr/bin/env python3

"""
This module contains the Auth class used for authentication
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Auth class for authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This function requires authentication for a given path

        :param path: The path to check for authentication
        :param excluded_paths: A list of paths that do not
        equire authentication
        :return: True if authentication is required, False otherwise
        """

        # Check if path or excluded_paths is None or empty
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        # Check if path is empty
        l_path = len(path)
        if l_path == 0:
            return True

        # Check if path ends with a slash
        slash_path = True if path[l_path - 1] == '/' else False

        # Add a slash to the path if it doesn't end with a slash
        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        # Check if the path is excluded
        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            # Check if the path is an exact match with an excluded path
            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                # Check if the path matches the excluded path with a wildcard
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        # If the path is not excluded, require authentication
        return True

    def authorization_header(self, request=None) -> str:
        """
        This function extracts the Authorization header from
        the request

        :param request: The request object
        :return: The Authorization header value, or None if the
        header is not present
        """

        # Check if request is None
        if request is None:
            return None

        # Get the Authorization header value from the request headers
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This function retrieves the current user from the request

        :param request: The request object
        :return: The current user, or None if no user is found
        """

        return None

    def session_cookie(self, request=None):
        """
        This function retrieves the session cookie from the request

        :param request: The request object
        :return: The session cookie value, or None if the cookie
        is not present
        """

        # Check if request is None
        if request is None:
            return None

        # Get the session cookie name from the environment variable
        SESSION_NAME = getenv("SESSION_NAME")

        # Check if session cookie name is None
        if SESSION_NAME is None:
            return None

        # Get the session cookie value from the request cookies
        session_id = request.cookies.get(SESSION_NAME)

        return session_id
