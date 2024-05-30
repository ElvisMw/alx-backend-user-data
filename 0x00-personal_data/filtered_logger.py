#!/usr/bin/env python3
"""Connect to secure database"""
import os
import mysql.connector
from mysql.connector import connection

def get_db() -> connection.MySQLConnection:
    """Returns a connector to the database."""
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=db_name
    )
