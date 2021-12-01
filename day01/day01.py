#!/usr/bin/env python
"""Day 1 of Advent of Code."""


def part1(input_data):
    """
    Returns solution to part 1 of day 1.

    Solution is the count of where input_data[N] is greater than
    input_data[N-1].

    Parameters
    ----------

    input_data : list of integers

    Returns
    -------

    : int
        Solution to part 1.

    """
    input_data = list(input_data)  # Initially, input_data is a generator.
    pairs = zip(input_data[1:], input_data[:-1])
    count = len([pair for pair in pairs if pair[0] > pair[1]])
    
    return count
