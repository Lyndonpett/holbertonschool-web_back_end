#!/usr/bin/env python3
"""Module for API authentication"""


from os import getenv
from flask import request
from typing import List, TypeVar


class Auth():
    """API authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns false if path is in excluded_paths"""
        if path is None or excluded_paths is None:
            return True

        if path in excluded_paths or f"{path}/" in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Returns flask request or none if no header"""
        if request is None or request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user or none"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None

        cookie = getenv('SESSION_NAME')

        return request.cookies.get(cookie)
