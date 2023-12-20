#!/usr/bin/env python3
"""
implement expiring we cache tracker
"""
from typing import Callable
import redis
import requests
from functools import wraps


db = redis.Redis()


def count_request(method: callable) -> callable:
    """
    count_request: count n of requests
    return: wraper func
    """
    @wraps(method)
    def wrapper(url):
        db.incr(f'count:{url}')
        html = db.get(f'cached:{url}')
        if html:
            return html.decode('utf-8')
        h = method(url)
        db.setex(f'cached:{url}', 10, h)
        return h
    return wrapper


@count_request
def get_page(url: str) -> str:
    """
    get page content
    """
    req = requests.get(url)
    return req.text
