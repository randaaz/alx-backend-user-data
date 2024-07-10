#!/usr/bin/env python3
""" UserSession class module.
"""
from models.base import Base


class UserSession(Base):
    """UserSession class that inherits from Base class.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """Constructor method for initializing a new UserSession instance."""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
