#!/usr/bin/env python
"""Day 1 of Advent of Code."""
from collections import deque


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
    pairs = zip(input_data[1:], input_data[:-1])
    count = len([pair for pair in pairs if pair[0] > pair[1]])
    
    return count


def part2(input_data):
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
    previous = deque(input_data[:3], maxlen=3)
    current = deque(input_data[1:4], maxlen=3)
    count = sum(current) > sum(previous)
    for next_value in input_data[4:]:
        previous.append(current[-1])
        current.append(next_value)
        if sum(current) > sum(previous):
            count += 1
    return count
