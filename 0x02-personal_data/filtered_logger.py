#!/usr/bin/env python3
"""RedactingFormatter class and helper functions"""

import logging
import re
from typing import List
import mysql.connector
from os import environ

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

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


def get_logger() -> logging.Logger:
    """Gets and returns a logger"""
    # create logger
    user_data = logging.getLogger("user_data")

    # set min to INFO
    user_data.setLevel(logging.INFO)
    user_data.propagate = False

    # create handler and set format with our PII_FIELDS
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))

    # add handler to logger
    user_data.addHandler(streamHandler)
    return user_data

def get_db() -> mysql.connector.connection.MySQLConnection:
    """Gets and returns a database connection"""
    db = mysql.connector.connect(
        host=environ.get("PERSONAL_DATA_DB_HOST"),
        user=environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=environ.get("PERSONAL_DATA_DB_PASSWORD"),
        database=environ.get("PERSONAL_DATA_DB_NAME")
    )
    return db
