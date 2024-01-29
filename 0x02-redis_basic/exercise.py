#!/usr/bin/env python3
"""a module that use redis"""
from uuid import uuid4
import redis
from typing import Union, Callable, Any


class Cache:
    """
    A cache class that instantiate redis client
    """

    def __init__(self) -> None:
        """ initialization of class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        A method that takes an arugment and return string
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Any:
        """A method that get a string argument"""
        data = self._redis.get(key)
        if data:
            if fn:
                return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """a method that get a string"""
        return self.get(key, lambda s: s.decode('utf-8'))

    def get_int(self, key: str):
        """a method that get an int"""
        return self.get(key, lambda i: int(i))
