#!/usr/bin/env python3

"""
This module contains the UserSession class, which represents
a user session in the application.
"""

from models.base import Base


class UserSession(Base):
    """
    The UserSession class represents a user session in the application.

    Attributes:
        user_id (str): The ID of the user associated with the session.
        session_id (str): The ID of the session.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize a UserSession instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        """Get the user ID from the keyword arguments and assign it
        to the instance variable 'user_id'."""
        self.user_id = kwargs.get('user_id')
        """Get the session ID from the keyword arguments and
        assign it to the instance variable 'session_id'."""
        self.session_id = kwargs.get('session_id')
