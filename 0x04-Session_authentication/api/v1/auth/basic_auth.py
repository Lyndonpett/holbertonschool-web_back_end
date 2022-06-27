#!/usr/bin/env python3
"""Module for basic authentication"""


from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts base64 authorization header"""
        if authorization_header is not None:
            if type(authorization_header) is str:
                if authorization_header.startswith('Basic '):
                    return authorization_header[6:]

        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decodes base64 header"""
        try:
            return b64decode(base64_authorization_header).decode('utf-8')

        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """Extracts the users email and password from header"""
        if decoded_base64_authorization_header is not None:
            if type(decoded_base64_authorization_header) is str:
                if ':' in decoded_base64_authorization_header:
                    return decoded_base64_authorization_header.split(':')

        return None, None

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Return user based on email and password"""
        if user_email is None or type(user_email) is not str:
            return None

        if user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            searchList = User.search({'email': user_email})

            for user in searchList:
                if user.is_valid_password(user_pwd):
                    return user

        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Overrides current_user method"""
        auth = request.headers.get('Authorization')
        header = self.extract_base64_authorization_header(auth)
        decoded_header = self.decode_base64_authorization_header(header)
        email, passwd = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(email, passwd)
