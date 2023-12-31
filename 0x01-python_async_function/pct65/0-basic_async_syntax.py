#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument (max_delay,
with a default value of 10) named wait_random that waits for a random delay
between 0 and max_delay (included and float value) seconds and eventually
returns it.

Use the random module.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait max of max_delay seconds and return the time waited."""
    wait: float = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: {} <number_of_seconds>'.format(sys.argv[0]))
        exit(98)
    print('Sleeping...\n')
    wait_random(int(sys.argv[1]))
