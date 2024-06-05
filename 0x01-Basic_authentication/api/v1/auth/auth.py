#!/usr/bin/env python3
<<<<<<< HEAD
"""Task-Authentication"""
from flask import request
from typing import List, TypeVar

=======
""" task 3."""
from flask import request
from typing import List, TypeVar

""" Define a type variable for the User class """
User = TypeVar('User')

>>>>>>> 04d2dbb053d1c08aa750854fc339fc13efd46040

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
            bool: True if the endpoint requires authentication,False otherwise
        """
<<<<<<< HEAD
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = True if path[l_path - 1] == '/' else False

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
=======
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request (Request): The Flask request object.

        Returns:
            str: The authorization header.
        """
        return None

    def current_user(self, request=None) -> User:
        """
        Retrieves the current user.

        Args:
            request (Request): The Flask request object.

        Returns:
            User: The current user.
>>>>>>> 04d2dbb053d1c08aa750854fc339fc13efd46040
        """
        return None
