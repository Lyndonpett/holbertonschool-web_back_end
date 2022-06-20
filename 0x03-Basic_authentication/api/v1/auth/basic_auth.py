#!/usr/bin/env python3
"""Module for basic authentication"""


from api.v1.auth.auth import Auth
import base64
from typing import Tuple


class BasicAuth(Auth):
    """Basic Auth class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts base64 authorization header"""
        if authorization_header is not None:
            if type(authorization_header) is str:
                if authorization_header.startswith('Basic '):
                    return authorization_header[6:]

        return None

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes base64 header"""
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')

        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Extracts the users email and password from header"""
        if decoded_base64_authorization_header is not None:
            if type(decoded_base64_authorization_header) is str:
                if ':' in decoded_base64_authorization_header:
                    return decoded_base64_authorization_header.split(':')

        return None, None
