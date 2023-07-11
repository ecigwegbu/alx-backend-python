#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
import typing
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being
    called."""

    if n == 0:
        return []

    #  spawn task_wait_random n times:
    result: list[float] = await asyncio.gather(*[task_wait_random(max_delay)
                                                 for _ in range(n)])
    return sorted(result)
