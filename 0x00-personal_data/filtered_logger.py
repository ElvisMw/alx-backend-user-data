#!/usr/bin/env python3
"""Redacting Formatter class"""
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class.

    This class is used to redact specific fields from log records.
    """

    # Redaction string
    REDACTION = "***"

    # Log format
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"

    # Field separator
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter.

        Args:
            fields (List[str]): List of fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record to redact PII fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record.
        """
        # Redact fields from the message
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)


def filter_datum(
    fields: List[str], redaction: str, datum: str, separator: str
) -> str:
    """
    Filter a datum by redacting specific fields.

    Args:
        fields (List[str]): List of fields to redact.
        redaction (str): The string to use for redaction.
        datum (str): The datum to filter.
        separator (str): The separator used in the datum.

    Returns:
        str: The filtered datum.
    """
    # Split the datum by the separator
    data = datum.split(separator)

    # Redact specified fields
    for idx, field in enumerate(fields):
        if field in data:
            data[idx] = redaction

    # Join the filtered data back together
    return separator.join(data)
