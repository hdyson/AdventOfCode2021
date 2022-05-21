#!/usr/bin/env python
"""Day 1 of Advent of Code."""
from collections import deque


def _to_ints(strings: list[str]) -> list[int]:
    return [int(string) for string in strings]


def part1(input_data: list[str]) -> int:
    """
    Returns solution to part 1 of day 1.

    Solution is the count of where input_data[N] is greater than
    input_data[N-1].

    Parameters
    ----------

    input_data : list of strings

    Returns
    -------

    : int
        Solution to part 1.

    """
    data = _to_ints(input_data)
    pairs = zip(data[1:], data[:-1])
    count = len([pair for pair in pairs if pair[0] > pair[1]])

    return count


def part2(input_data: list[str]) -> int:
    """
    Returns solution to part 1 of day 1.

    Solution is the count of where input_data[N] is greater than
    input_data[N-1].

    Parameters
    ----------

    input_data : list of strings

    Returns
    -------

    : int
        Solution to part 1.

    """
    data = _to_ints(input_data)
    previous = deque(data[:3], maxlen=3)
    current = deque(data[1:4], maxlen=3)
    count = int(sum(current) > sum(previous))
    for next_value in data[4:]:
        previous.append(current[-1])
        current.append(next_value)
        if sum(current) > sum(previous):
            count += 1
    return count
