#!/usr/bin/env python3

"""
This module contains the SessionExpAuth class, which inherits from
SessionAuth and implements session management with an expiration time.
"""

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from models.user import User
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class that inherits from SessionAuth and implements
    session management with an expiration time.
    """

    def __init__(self):
        """
        Initializes a SessionExpAuth instance.
        """

        # Get the session duration from the environment variable
        SESSION_DURATION = getenv('SESSION_DURATION')

        try:
            session_duration = int(SESSION_DURATION)
        except Exception:
            session_duration = 0

        self.session_duration = session_duration

    def create_session(self, user_id=None):
        """
        Creates a session for a given user ID and adds it to the dictionary.

        Args:
            user_id (str): The user ID to create a session for.

        Returns:
            str: The session ID.
        """

        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Retrieves the user ID associated with a session ID.

        Args:
            session_id (str): The session ID to retrieve the user ID for.

        Returns:
            str: The user ID associated with the session ID, or
            None if the session ID is not found or has expired.
        """

        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id.keys():
            return None

        session_dictionary = self.user_id_by_session_id.get(session_id)

        if session_dictionary is None:
            return None

        if self.session_duration <= 0:
            return session_dictionary.get('user_id')

        created_at = session_dictionary.get('created_at')

        if created_at is None:
            return None

        expired_time = created_at + timedelta(seconds=self.session_duration)

        if expired_time < datetime.now():
            return None

        return session_dictionary.get('user_id')
