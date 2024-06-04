#!/usr/bin/env python3
""" task 3"""
from flask import request
from typing import List, TypeVar

""" Define a type variable for the User class """
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
        """
        return None
