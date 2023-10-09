#!/usr/bin/env python3
"""Async task: wait_random
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """argument with default value of 10
    that waits for a random delay between 0 ans max_delay
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay