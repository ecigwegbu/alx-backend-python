#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    res = await task
    print("Task Result: ", res)
    print(task.__class__)

asyncio.run(test(5))
