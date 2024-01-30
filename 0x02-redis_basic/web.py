#!/usr/bin/env python3
"""a module that """
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
    return requests.get(url)

"""
if __name__ == '__main__':
    slow_url = 'http://slowwly.robertomurray.co.uk'
    
    for _ in range(3):
        content = get_page(slow_url)
        print(f'Content for {slow_url}\n{content}')
        time.sleep(5)

        access_count_key = f'count:{slow_url}'
        total_access_count = cache.get(access_count_key)
        print(f"Total access count for {slow_url}: {total_access_count.decode('utf-8')}")
"""
