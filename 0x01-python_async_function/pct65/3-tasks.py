#!/usr/bin/env python3
"""
3. Tasks
"""
import asyncio
import random
import time
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Import wait_random from 0-basic_async_syntax.
    Write a function (do not create an async function, use the regular
    function syntax to do this) task_wait_random that takes an integer
    max_delay and returns a asyncio.Task."""

    wait: float = random.random() * max_delay
    time.sleep(wait)

    return asyncio.Task
