#!/usr/bin/env python3

"""
This module contains the SessionDBAuth class, which inherits from
SessionExpAuth and implements session management with a database.
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class that inherits from SessionExpAuth and implements
    session management with a database.
    """

    def create_session(self, user_id=None):
        """
        Creates a session for a given user ID and saves it to the
        UserSession model.

        Args:
            user_id (str): The user ID to create a session for.

        Returns:
            str: The session ID.
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        kwargs = {'user_id': user_id, 'session_id': session_id}
        user_session = UserSession(**kwargs)
        user_session.save()
        UserSession.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Retrieves the user ID associated with a session ID from the
        UserSession model.

        Args:
            session_id (str): The session ID to retrieve the user ID for.

        Returns:
            str: The user ID associated with the session ID, or None
            if the session ID is not found.
        """
        if session_id is None:
            return None

        UserSession.load_from_file()
        user_session = UserSession.search({
            'session_id': session_id
        })

        if not user_session:
            return None

        user_session = user_session[0]

        expired_time = user_session.created_at + \
            timedelta(seconds=self.session_duration)

        if expired_time < datetime.utcnow():
            return None

        return user_session.user_id

    def destroy_session(self, request=None):
        """
        Destroys a session for a given request by removing it from the
        UserSession model.

        Args:
            request (Request): The request object.

        Returns:
            bool: True if the session was successfully destroyed,
            False otherwise.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        user_session = UserSession.search({
            'session_id': session_id
        })

        if not user_session:
            return False

        user_session = user_session[0]

        try:
            user_session.remove()
            UserSession.save_to_file()
        except Exception:
            return False

        return True
