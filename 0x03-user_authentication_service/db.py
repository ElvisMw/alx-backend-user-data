#!/usr/bin/env python3

"""
This module contains the DB class that provides methods for
interacting with the
database.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from user import Base, User


class DB:
    """
    Class that provides methods for interacting with the database.
    """

    def __init__(self):
        """
        Initializes the database and creates the session.
        """

        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
        Returns the session object. Creates a new session if
        one doesn't exist.
        """

        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user to the database.

        Args:
            email (str): The user's email.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The newly created user object.
        """

        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user in the database based on the provided parameters.

        Args:
            **kwargs: Keyword arguments representing the column
            names and their corresponding values.

        Returns:
            User: The user object if found, raises NoResultFound if not found.

        Raises:
            InvalidRequestError: If an invalid column name is provided.
        """

        if not kwargs:
            raise InvalidRequestError

        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates a user in the database.

        Args:
            user_id (int): The id of the user to update.
            **kwargs: Keyword arguments representing the column names
            and their corresponding new values.

        Raises:
            ValueError: If an invalid column name is provided.
        """

        user = self.find_user_by(id=user_id)

        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise ValueError

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.commit()
