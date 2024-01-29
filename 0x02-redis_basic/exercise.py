#!/usr/bin/env python3
"""a module that use redis"""
from uuid import uuid4
import redis
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ a function that count how many times called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """wrapper"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """a function that store the history of inputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """wrapper"""
        input_key = f'{method.__qualname__}:inputs'
        output_key = f'{method.__qualname__}:outputs'
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable) -> Any:
    """a function that display the history of calls"""
    fn = method.__qualname__
    input_key = f'{fn}:inputs'
    output_key = f'{fn}:outputs'
    cache = method.__self__
    num = cache.get_int(fn)
    output_list = cache._redis.lrange(output_key, 0, -1)
    input_list = cache._redis.lrange(input_key, 0, -1)
    print('{} was called {} times:'.format(fn, num))
    for lin, lout in zip(input_list, output_list):
        lin_decode = lin.decode('utf-8')
        lout_decode = lout.decode('utf-8')
        print('{}(*{}) -> {}'.format(fn, lin_decode, loutdecode))


class Cache:
    """
    A cache class that instantiate redis client
    """

    def __init__(self) -> None:
        """ initialization of class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
