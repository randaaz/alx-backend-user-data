#!/usr/bin/env python3
"""
Module for hashing passwords and validating them using bcrypt.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a password using bcrypt. """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates a password against a hashed password. """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
