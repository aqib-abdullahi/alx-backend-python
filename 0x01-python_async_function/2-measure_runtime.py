#!/usr/bin/env python3
'''measure_time module
'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''return total time taken to execute wait_n divided by n
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    duration = time.time() - start_time
    return duration/n