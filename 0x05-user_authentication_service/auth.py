#!/usr/bin/env python3
"""Auth module for the User Authentication Service"""


from bcrypt import checkpw, hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            passwrd = _hash_password(password)
            user = self._db.add_user(email, passwrd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a user login"""
        try:
            user = self._db.find_user_by(email=email)
            passwrd = password.encode('utf-8')
            return checkpw(passwrd, user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for a user"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return hashpw(password.encode(), gensalt())

def _generate_uuid() -> str:
    """Generate a UUID"""
    return str(uuid.uuid4())
