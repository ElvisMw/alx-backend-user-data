#!/usr/bin/env python3

"""Module for obfuscating log messages."""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated.

    :param fields: A list of fields to be obfuscated.
    :param redaction: The redaction string to replace the obfuscated fields.
    :param message: The log message to be obfuscated.
    :param separator: The character used to separate the
    fields in the log message.
    :return: The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"

    return re.sub(pattern, lambda x:
                  x.group().split('=')[0] + '=' + redaction, message)
