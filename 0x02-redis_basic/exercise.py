#!/usr/bin/env python3
"""A Class that writes strings to Redis"""
import redis
from typing import Union, Optional, Callable
import uuid


class Cache():
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis"""
        # Generate a random UUID
        random_key = uuid.uuid4()

        # Convert the UUID to a string
        random_key_str = str(random_key)

        # Stores data into redis
        self._redis.set(random_key_str, data)

        return random_key_str

    def get_str(self, key: str) -> str:
        """Retrieves a string from Redis."""
        # Retrieve the value from Redis
        value = self._redis.get(key)
        if value is None:
            return None
        # Convert bytes to string
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Retrieves an integer from Redis."""
        # Retrieve the value from Redis
        value = self._redis.get(key)
        if value is None:
            return None
        # Convert bytes to integer
        return int(value)

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float]]] = None) -> Union[str, float, int, None]:
        """Retrieves data from Redis and applies an optional conversion function."""
        # Get the data from Redis
        value = self._redis.get(key)
        if value is None:
            return None

        # If a conversion function is provided, apply it
        if fn:
            return fn(value)

        return value
