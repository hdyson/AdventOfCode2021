#!/usr/bin/env python
"""Day 2 of Advent of Code."""


def parse_line(line: str) -> tuple[str, int]:
    """Return dict where key is the direction and the value is the magnitude.

    Assumes input is of form "direction N" where N is the magnitude.

    Parameters
    ----------

    line : str

    Returns
    -------

    : dict
    """
    key, value = line.split()
    return key, int(value)


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
    moves: dict[str, int] = dict()
    for line in input_data:
        direction, magnitude = parse_line(line)
        if direction not in moves.keys():
            moves[direction] = magnitude
        else:
            moves[direction] = moves[direction] + magnitude
    depth = moves['down'] - moves['up']
    return depth * moves['forward']


def part2(input_data: list[str]) -> int:
    aim = 0
    depth = 0
    forward = 0
    for line in input_data:
        direction, magnitude = parse_line(line)
        if direction == 'down':
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude
        elif direction == 'forward':
            depth += aim * magnitude
            forward += magnitude
    return depth * forward
