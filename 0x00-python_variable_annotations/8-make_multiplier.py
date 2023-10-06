#!/usr/bin/env python3
"""Task8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier returns a
    function that multiplies a
    float by multiplier.
    """
    def multiplying_function(x: float) -> float:
        return x * multiplier

    return multiplying_function
