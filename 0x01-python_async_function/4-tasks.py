#!/usr/bin/env python3
"""
4. Tasks:
Let's execute multiple coroutines at the same time with async
"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[asyncio.Task]:
    """Take the code from wait_n and alter it into a new function
    task_wait_n. The code is nearly identical to wait_n except
    task_wait_random is being called:

    Import wait_random from the previous python file that you’ve written
    and write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n times
    with the specified max_delay.

    wait_n should return the list of all the delays (float values). The list
    of the delays should be in ascending order without using sort() because
    of concurrency."""

    #  spawn wait_random n times:
    result: list[asyncio.Task] = await asyncio.gather(*[task_wait_random(
                                    max_delay) for _ in range(n)])
    return sorted(result)
