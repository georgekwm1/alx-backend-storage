#!/usr/bin/env python3
"""A Class that writes strings to Redis"""
import redis
from typing import Union, Optional, Callable
import uuid


class Cache():
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]):
        """Stores data in redis"""
        # Generate a random UUID
        random_key = uuid.uuid4()

        # Convert the UUID to a string
        random_key_str = str(random_key)

        # Stores data into redis
        self._redis.set(random_key_str, data)

        return random_key_str

    def get(self, key: str, fn: Optional[Callable])
