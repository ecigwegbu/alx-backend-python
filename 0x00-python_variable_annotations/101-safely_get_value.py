#!/usr/bin/env python3
"""11. More involved type annotations"""
import typing


def safely_get_value(dct, key, default=None):
    """Given the parameters and the return values, add type annotations
    to the function. Hint: look into TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
