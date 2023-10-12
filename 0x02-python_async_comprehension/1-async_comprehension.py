#!/usr/bin/env python3
"""async_comprehension task2
"""
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """collects 10 random numbers using async comprehensing
    over async_generator and return the 10 random numbers
    """
    result = []
    async for i in async_generator():
        result.append(i)

    return result
