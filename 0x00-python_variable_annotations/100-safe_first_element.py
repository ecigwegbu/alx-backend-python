#!/usr/bin/env python3
from typing import Any, Sequence, Union

"""10. Duck typing - first element of a sequence"""


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    """Augument code with duck-typing"""
    if lst:
        return lst[0]
    else:
        return None
