#!/usr/bin/env python3

"""5. Complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    """Write a type-annotated function sum_list which takes a
    list input_list of floats as argument and returns their sum
    as a float."""
    listSum: float = 0
    for item in input_list:
        listSum += item
    return listSum
