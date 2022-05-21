#!/usr/bin/env python
"""Day 3 of Advent of Code."""
import pandas as pd
import scipy.stats


def part1(input_data: list[str]) -> int:
    """
    Return product of forward movements and depth.

    Parameters
    ----------

    input_data : list of str

    Returns
    -------

    : int

    """
    df = pd.DataFrame.from_records(input_data)
    most_common_bits, _ = scipy.stats.mode(df, axis=0)
    most_common_bits = most_common_bits[0]
    epsilon_rate = 0
    gamma_rate = 0
    for exponent, bit in enumerate(reversed(most_common_bits)):
        epsilon_rate += (2 ** exponent) * int(bit)
        gamma_rate += (2 ** exponent) * (1 - int(bit))
    return epsilon_rate * gamma_rate


def part2(input_data: list[str]) -> None:
    pass
