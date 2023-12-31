#!/usr/bin/env python3
"""async_comprehension task2
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random numbers using async comprehensing
    over async_generator and return the 10 random numbers
    """
    # result = []
    # async for i in async_generator():
    #     result.append(i)
    #
    # return result
    return [num async for num in async_generator()]
