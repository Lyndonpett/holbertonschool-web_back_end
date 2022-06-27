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
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


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


def main():
    """Connects to db, gets info, and displays it"""
    logger = get_logger()
    db = get_db()

    # create cursor, execute queries in all rows
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")

    for row in cursor:
        # list of tuples
        tupleList = row.items()
        # transform to list of strings with PII_FIELDS
        str = "; ".join(f"{tuple[0]}={tuple[1]}" for tuple in tupleList)
        logger.info(str)

    db.close()


if __name__ == "__main__":
    main()
