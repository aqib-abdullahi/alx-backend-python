#!/usr/bin/env python3
"""Task 6
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums up all integers and n a mixed list
    """
    return float(sum(mxd_lst))
