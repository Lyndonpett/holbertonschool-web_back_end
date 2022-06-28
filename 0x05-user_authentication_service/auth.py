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

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get a user from a session ID"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, session_id: str) -> None:
        """Destroys a session from id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Get a reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update a user password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            pw = _hash_password(password)
            self._db.update_user(user.id, hashed_password=pw, reset_token=None)
        except Exception:
            raise ValueError


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return hashpw(password.encode(), gensalt())


def _generate_uuid() -> str:
    """Generate a UUID"""
    return str(uuid.uuid4())
