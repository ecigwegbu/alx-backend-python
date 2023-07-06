#!/usr/bin/env python3
"""6. Complex types - mixed list"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Write a type-annotated function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float."""

    return sum(mxd_lst)
