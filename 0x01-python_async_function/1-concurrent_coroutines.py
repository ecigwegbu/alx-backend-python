#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Import wait_random from the previous python file that you’ve written
    and write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n times
    with the specified max_delay.

    wait_n should return the list of all the delays (float values). The list
    of the delays should be in ascending order without using sort() because
    of concurrency."""

    # spawn wait_random n times:
    result: typing.List[float] = []
    i: int = 0
    for i in range(n):
        result.append(await wait_random(max_delay))
    return result


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        pass
        #  print('Usage: {} <number_of_seconds>'.format(sys.argv[0]))
        #  exit(98)
    #  code here
    pass
