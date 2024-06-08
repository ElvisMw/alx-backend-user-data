#!/usr/bin/env python3
"""Session Authentication Module"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    Session Authentication Class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session for a given user ID

        Args:
            user_id (str): The user ID to create a session for

        Returns:
            str: The session ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user ID associated with a session ID

        Args:
            session_id (str): The session ID to retrieve the user ID for

        Returns:
            str: The user ID associated with the session ID, or
            None if the session ID is not found
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Retrieves the current user from the request

        Args:
            request (Request): The request object

        Returns:
            User: The current user, or None if the request is None
        """
        session_id = self.session_cookie(request)

        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Destroys a session for a given request

        Args:
            request (Request): The request object

        Returns:
            bool: True if the session was successfully destroyed,
            False otherwise
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
