#!/usr/bin/env python3
"""
redis storage class
"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """
    redis storage class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store: generate random key
        Args:
            data: input data
        return: (string) random string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        get: retrieeve fromdb
        Args:
            key: unique key string
            fn: optional convertion func
        return: data
        """
        data = self._redis.get(key)

        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        convertion function for string
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        convertion function for integer
        """
        return self.get(key, fn=int)

