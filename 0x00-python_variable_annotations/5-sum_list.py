#!/usr/bin/python3

from typing import List


def sum_list(input_list: List[float]) -> float:
    if input_list is None:
        return 0
    return sum(input_list)
