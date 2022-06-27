#!/usr/bin/env python3
"""Auth module for the User Authentication Service"""


from bcrypt import checkpw, hashpw, gensalt
from db import DB


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return hashpw(password.encode(), gensalt())
