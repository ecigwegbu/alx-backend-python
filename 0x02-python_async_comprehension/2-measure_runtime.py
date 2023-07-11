#!/usr/bin/env python3
"""
2. Run time for parallel comprehension
"""
import asyncio
import time
import typing
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds, explain it to
    yourself.
    """
    start_time: float = time.perf_counter()
    await asyncio.gather(
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension())
    )
    finish_time: float = time.perf_counter()
    return finish_time - start_time
