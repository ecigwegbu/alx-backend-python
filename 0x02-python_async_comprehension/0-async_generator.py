#!/usr/bin/env python3
"""
0.Async generator: Illustrate use of async generators in programs
"""
import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, type[None]]:
    """Write a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module."""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
