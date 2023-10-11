#!/usr/bin/env python3
"""async_generator module
"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
