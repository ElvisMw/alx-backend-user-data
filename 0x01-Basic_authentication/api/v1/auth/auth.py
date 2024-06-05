#!/usr/bin/env python3
"""Task-Authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    This class provides methods for validating if an endpoint requires
    authentication and for handling authorization headers.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Validates if an endpoint requires authentication.

        Args:
            path (str): The path of the endpoint.
            excluded_paths (List[str]): The list of paths that are excluded
                from authentication.

        Returns:
            bool: True if the endpoint requires authentication, False otherwise
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = path[l_path - 1] == '/'
        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Handles the authorization header.

        Args:
            request (flask.Request, optional): The request object.
                Defaults to None.

        Returns:
            str: The value of the authorization header or None if the request
                is None or the header is not found.
        """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Validates the current user.

        Args:
            request (flask.Request, optional): The request object
                Defaults to None.

        Returns:
            TypeVar('User'): The user instance or None if the request is None
        """
        return None
