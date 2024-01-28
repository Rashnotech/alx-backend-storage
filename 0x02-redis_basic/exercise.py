#!/usr/bin/env python3
"""a module that use redis"""
from uuid import uuid4
import redis
from typing import Union


class Cache:
    """
    A cache class that instantiate redis client
    """

    def __init__(self) -> None:
        """ initialization of class"""
        self._redis = redis.Redis()
        self._redis.flushall()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        A method that takes an arugment and return string
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
