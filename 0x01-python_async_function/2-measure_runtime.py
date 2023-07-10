#!/usr/bin/env python3
"""
2. Measure the runtime
"""
import asyncio
import random
import time
import typing
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """From the previous file, import wait_n into 2-measure_runtime.py.
    Create a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should return a float.
    Use the time module to measure an approximate elapsed time."""

    t0: float = time.perf_counter()  # start time
    await wait_n(n, max_delay)
    t1: float = time.perf_counter()  # finish time
    total_time: float = t1 - t0

    return total_time / float(n)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: {} <number_of_seconds>'.format(sys.argv[0]))
        exit(98)
    print('Sleeping...\n')
    wait_random(int(sys.argv[1]))
