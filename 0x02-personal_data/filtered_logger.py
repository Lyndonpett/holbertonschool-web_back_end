#!/usr/bin/env python3
"""RedactingFormatter class and helper functions"""

import logging
import re
from typing import List

class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize RedactingFormatter class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """Format log record"""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)

def filter_datum(fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    """Filter using regex"""
    for field in fields:
        regexString = f"(?<={field}=).*?(?={separator})"
        message = re.sub(regexString, redaction, message)
    return message
