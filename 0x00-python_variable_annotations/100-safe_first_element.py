#!/usr/bin/env python3
"""Advanced task100
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first content in a list if any, else none
    """
    if lst:
        return lst[0]
    else:
        return None
