#!/usr/bin/env python3
"""a module that keep track the number of count"""
import requests
from functools import wraps
import time
import redis
from typing import Callable, Any


cache = redis.Redis()


def cache_result(func) -> Callable:
    """cach result"""
    @wraps(func)
    def wrapper(url) -> Callable:
        # check if the result is already cached
        cache_key = f'result:{url}'
        count_key = f'count:{url}'
        cache.incr(count_key)
        cached_result = cache.get(cache_key)
        if cached_result:
            return cached_result.decode('utf-8')
        result = func(url)
        cache.set(count_key, 0)
        cache.setex(cache_key, 10, result)
        return result
    return wrapper


@cache_result
def get_page(url: str) -> str:
    """ a module that get page in 10 seconds"""
    return requests.get(url)
