#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(number: float) -> float:
        return multiplier * number

    return multiplier_func
