#!/usr/bin/env python3
"""11. More involved type annotations"""
from typing import Union, TypeVar, Any, Mapping


def safely_get_value(dct: Mapping, key: Any, default: type[None] = None)\
        -> Any:

    """Given the parameters and the return values, add type annotations
    to the function. Hint: look into TypeVar"""

    if key in dct:
        return dct[key]
    else:
        return default
