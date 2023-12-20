#!/usr/bin/env python3
"""
redis storage class
"""
import redis
from typing import Union, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count_calls: count times method is clled
    method: method of Cache class
    return: wrppaer func
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wrapper: increment count of method call. redis
        return value of current method
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history: store history of inps and outs of func
    Args:
        method: function to track
    return: wrapper function
    """
    key = method.__qualname__
    input_list = key + ":inputs"
    output_list = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        store to list (input_list)
        save output
        store ouput (output_list)
        return output
        """
        self._redis.rpush(input_list, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(output_list, str(output))
        return output
    return wrapper


def replay(method: Callable):
    """
    replay: history of a function
    Args:
        method: funtion to track
    """
    db = redis.Redis()
    key = method.__qualname__
    n = db.get(key).decode('utf-8')
    print(f"{key} was called {n} times")
    i = db.lrange(key + ":inputs", 0, -1)
    o = db.lrange(key + ":outputs", 0, -1)
    for j, k in zip(i, o):
        print(f"{key}(*{j.decode('utf-8')}) -> {k.decode('utf-8')}")


class Cache:
    """
    redis storage class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
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

    def get_str(self, key: str) -> str:
        """
        convertion function for string
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        convertion function for integer
        """
        return self.get(key, fn=int)
