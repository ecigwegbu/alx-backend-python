#!/usr/bin/env python3
"""
0.Async generator: Illustrate use of async generators in programs
"""
import asyncio
from random import random
import typing


async def async_generator() -> float:
    """Write a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module."""

    i: int = 0
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10.0
