#!/usr/bin/env python3
""""8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Write a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier."""
    def cb(fl: float) -> float:
        """multiply float by multiplier"""
        return fl * multiplier
    return cb
