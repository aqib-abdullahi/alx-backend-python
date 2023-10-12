#!/usr/bin/env python3
"""measure_runtime task2
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes async_comprehension four times using asyncio.gather
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    finish_time = time.time() - start_time
    return finish_time
