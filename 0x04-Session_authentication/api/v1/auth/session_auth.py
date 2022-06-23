#!/usr/bin/env python3
"""Class for Session Authentication"""


from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """Class for Session Auth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates session ID for user ID"""
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid4())

        self.user_id_by_session_id.update({session_id: user_id})

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns user id based on session id"""
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns user id based on cookie"""
        session_id = self.session_cookie(request)

        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes user session aka logs out"""
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if session_id and self.user_id_for_session_id(session_id):
            self.user_id_by_session_id.pop(session_id)
            return True

        return False
