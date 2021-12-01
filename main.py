#!/usr/bin/env python
"""Launcher to run all days of advent of code 2021."""
from common import load_integers
from day01 import day01


def main():
    day_1_input = load_integers("./inputs/day01.txt")
    day_1_part_1_result = day01.part1(day_1_input)
    print(f"day 1 part 1: {day_1_part_1_result}")


if __name__ == "__main__":
    main()
