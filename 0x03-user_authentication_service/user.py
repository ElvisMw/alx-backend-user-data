#!/usr/bin/env python3

"""
This module contains the User class that defines the schema
for the users table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    This class represents a user in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (Integer): The primary key for the user.
        email (String): The email of the user.
        hashed_password (String): The hashed password of the user.
        session_id (String): The session ID of the user.
        reset_token (String): The reset token for the user.
    """

    # Define the table name
    __tablename__ = 'users'

    # Define the columns
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
