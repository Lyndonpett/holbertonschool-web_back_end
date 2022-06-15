#!/usr/bin/env python3
"""RedactingFormatter class and helper functions"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    """Filter using regex"""
    for field in fields:
        regexString = f"(?<={field}=).*?(?={separator})"
        message = re.sub(regexString, redaction, message)
    return message
