#!/usr/bin/env python3
""" Define which routes don't need authentication """
from flask import request
from typing import List, TypeVar

"""Define a type variable for the User class """
User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the endpoint requires authentication

        Args:
            path (str): The path of the endpoint.
            excluded_paths (List[str]): List of paths excluded
            from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
            elif path.startswith(excluded_path):
                return False

        return True
