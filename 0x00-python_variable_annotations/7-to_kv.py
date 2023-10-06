#!/usr/bin/env python3
"""Taask 7
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """creates tuple with string and int or float
    """
    return (k, v ** 2)
