#!/usr/bin/env python3
"""Module for basic authentication"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts base64 authorization header"""
        if authorization_header is not None:
            if type(authorization_header) is str:
                if authorization_header.startswith('Basic '):
                    return authorization_header[6:]

        return None
