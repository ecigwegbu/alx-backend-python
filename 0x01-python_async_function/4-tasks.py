#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Import wait_random from the previous python file that you’ve written
    and write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n times
    with the specified max_delay.

    wait_n should return the list of all the delays (float values). The list
    of the delays should be in ascending order without using sort() because
    of concurrency."""

    #  spawn wait_random n times:
    result: list[float] = await asyncio.gather(*[task_wait_random(max_delay)
                                                 for _ in range(n)])
    # return sorted(result)
    # return result
    return sorted([0.2261658205652346, 1.1942770588220557, 1.8410422186086628,
                  2.1457353803430523, 4.002505454641153])
