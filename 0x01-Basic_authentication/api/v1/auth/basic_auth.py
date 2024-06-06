#!/usr/bin/env python3
""" This module defines the BasicAuth class which is used for
handling Basic Authentication.
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """This class provides methods for handling Basic
    Authentication.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """This method extracts the Base64 encoded value
        from the Authorization header.

        Args:
            authorization_header (str): The Authorization header.

        Returns:
            str: The Base64 encoded value or None if the header
                is None or does not start with 'Basic '.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """This method decodes the Base64 encoded value.

        Args:
            base64_authorization_header (str): The Base64 encoded value.

        Returns:
            str: The decoded value or None if the value is None
                or not a string.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Extract the user email and password from the Base64 decoded value

        Args:
            decoded_base64_authorization_header (str): The Base64 decoded value

        Returns:
            tuple: The user email and password or None if the value is None
                or does not contain a colon.
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the value at the first colon and get the first and second parts
        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Get the User instance based on the email and password

        Args:
            user_email (str): The user email.
            user_pwd (str): The user password.

        Returns:
            User: The User instance or None if the email or password is None
                or not a string.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method overloads the current_user method in the Auth class
        and retrieves the User instance for a request.

        Args:
            request (flask.Request, optional): The request object.
                Defaults to None.

        Returns:
            User: The User instance or None if the request is None,
                the Authorization header is None or empty, the Base64
                encoded value is None or empty, the decoded value is None
                or empty, the user email and password are None or empty, or
                the user is not found.
        """
        auth_header = self.authorization_header(request)

        if not auth_header:
            return None

        encoded = self.extract_base64_authorization_header(auth_header)

        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)

        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)

        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)

        return user
