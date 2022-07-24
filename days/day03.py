#!/usr/bin/env python
"""Day 3 of Advent of Code."""
import pandas as pd
import numpy as np
import scipy.stats


def part1(input_data: list[str]) -> int:
    """
    Return product of epsilon_rate and gamma_rate.

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


def part2(input_data: list[str]) -> int:
    """
    Return product of oxygen and co2 ratings.

    Parameters
    ----------

    input_data : list of str

    Returns
    -------

    : int
    """
    oxygen_rating = 0
    co2_rating = 0

    data = np.vstack([np.fromiter(line, dtype=int) for line in input_data])
    for column in range(data.shape[1]):
        number_of_lines = data.shape[0]
        if sum(data[:, column]) >= number_of_lines / 2.:
            data = data[data[:, column] == 1]
        else:
            data = data[data[:, column] == 0]
        if data.shape[0] == 1:
            break
    for exponent, bit in enumerate(reversed(data[0])):
        oxygen_rating += (2 ** exponent) * int(bit)

    data = np.vstack([np.fromiter(line, dtype=int) for line in input_data])
    for column in range(data.shape[1]):
        number_of_lines = data.shape[0]
        if sum(data[:, column]) < number_of_lines / 2.:
            data = data[data[:, column] == 1]
        else:
            data = data[data[:, column] == 0]
        if data.shape[0] == 1:
            break
    for exponent, bit in enumerate(reversed(data[0])):
        co2_rating += (2 ** exponent) * int(bit)

    return oxygen_rating * co2_rating
