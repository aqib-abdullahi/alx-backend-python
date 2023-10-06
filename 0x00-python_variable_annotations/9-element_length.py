#!/usr/bin/env python3
"""Task9
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """calcs the length of each element in the input list.
    """
    return [(i, len(i)) for i in lst]
